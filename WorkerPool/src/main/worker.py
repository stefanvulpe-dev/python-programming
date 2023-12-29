"""Worker process for RQ workers

Usage:
python worker.py [-q <queue_name>]

Arguments:
-q, --queue: Redis queue name

Exit codes:
1: no .env file found
1: cannot connect to Redis
1: unexpected error

Example:
python worker.py -q worker-pool-queue

Author:
Stefan Vulpe

Date:
2023/12/28
"""


import argparse
import asyncio
import json
import os
import sys

import aiofiles
import aiohttp
from dotenv import dotenv_values
from redis import Redis

from src.utils.utils import get_logger, ping_redis


def parse_args():
    """Parse command line arguments

    Parse command line arguments and return the parsed arguments.

    Returns:
    argparse.Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(prog='worker.py', description='Worker process for RQ workers')
    parser.add_argument('-q', '--queue', type=str, default='worker-pool-queue', help='Redis queue name')
    return parser.parse_args()


async def save_webpage(url, disk_location, logger):
    """Saves a webpage to disk

    Saves a webpage to disk using aiohttp and aiofiles.

    Args:
    url (str): webpage url
    disk_location (str): path to the output file
    logger (logging.Logger): logger object

    Returns:
    None
    """
    try:
        os.path.normpath(disk_location)
    except TypeError as e:
        logger.error(f'Invalid output directory: {e}')
        return

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.read()

        async with aiofiles.open(disk_location, 'wb') as f:
            await f.write(content)
    except Exception as e:
        logger.error(f'Unexpected error downloading page {url}: {e}')


def download_webpage(url, disk_location, logger):
    """Downloads a webpage

    Downloads a webpage using asyncio and saves it to disk.

    Args:
    url (str): webpage url
    disk_location (str): path to the output file
    logger (logging.Logger): logger object

    Returns:
    None
    """
    if sys.version_info < (3, 10):
        loop = asyncio.get_event_loop()
    else:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()

        asyncio.set_event_loop(loop)

    loop.run_until_complete(save_webpage(url, disk_location, logger))


def process_job(job, logger):
    """Processes a job

    Processes a job by downloading a webpage.

    Args:
    job (tuple): job tuple
    logger (logging.Logger): logger object

    Returns:
    None
    """
    logger.info(f'Worker {os.getpid()} processing job: {job}')
    job_content = json.loads(job[1])
    output_dir = job_content['DiskLocation']
    page_url = f'https://www.{job_content['link'].lower()}'

    os.makedirs(output_dir, exist_ok=True)

    download_webpage(page_url, f'{output_dir}\\{job_content['link'].lower()}_index.html', logger)

    logger.info(f'Worker {os.getpid()} finished processing job: {job}')


def work(redis_conn, queue_name, logger):
    """Worker process

    Worker process that gets jobs from the queue and processes them.

    Args:
    redis_conn (Redis): Redis connection object
    queue_name (str): name of the queue
    logger (logging.Logger): logger object

    Returns:
    None
    """
    while True:
        job = redis_conn.brpop(queue_name, 30)
        if job is None:
            break
        logger.info(f'Worker {os.getpid()} got job: {job}')
        process_job(job, logger)

    logger.info(f'Worker {os.getpid()} got no job in 30 seconds, exiting')


def main():
    """Main function

    Main function that spawns the worker process.

    Returns:
    None
    """
    logger = get_logger(f'worker-{os.getpid()}', f'./static/logs/worker-{os.getpid()}.log')
    args = parse_args()

    logger.info(f'Worker {os.getpid()} started')

    if dotenv_values('.env') == {}:
        logger.error('No .env file found')
        exit(1)

    redis_conn = Redis(host=dotenv_values('.env')['REDIS_HOST'], port=dotenv_values('.env')['REDIS_PORT'],
                       decode_responses=True)

    ping_redis(redis_conn, logger)

    work(redis_conn, args.queue, logger)

    logger.info(f'Worker {os.getpid()} finished')


if __name__ == '__main__':
    main()
