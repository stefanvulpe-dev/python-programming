import argparse
import asyncio
import json
import os

import aiofiles
import aiohttp
import requests
from dotenv import dotenv_values
from redis import Redis

from src.utils import get_logger, ping_redis


def parse_args():
    parser = argparse.ArgumentParser(prog='worker.py', description='Worker process for RQ workers')
    parser.add_argument('-q', '--queue', type=str, default='worker-pool-queue', help='Redis queue name')
    return parser.parse_args()


async def save_webpage(url, disk_location, logger):
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
    loop = asyncio.get_event_loop()
    loop.run_until_complete(save_webpage(url, disk_location, logger))


def process_job(job, logger):
    logger.info(f'Worker {os.getpid()} processing job: {job}')
    job_content = json.loads(job[1])
    output_dir = job_content['DiskLocation']
    page_url = f'https://www.{job_content['link'].lower()}'

    os.makedirs(output_dir, exist_ok=True)

    download_webpage(page_url, f'{output_dir}\\{job_content['link'].lower()}_index.html', logger)

    logger.info(f'Worker {os.getpid()} finished processing job: {job}')


def work(redis_conn, queue_name, logger):
    while True:
        job = redis_conn.brpop(queue_name, 30)
        if job is None:
            break
        logger.info(f'Worker {os.getpid()} got job: {job}')
        process_job(job, logger)

    logger.info(f'Worker {os.getpid()} got no job in 30 seconds, exiting')


def main():
    logger = get_logger(f'worker-{os.getpid()}', f'./logs/worker-{os.getpid()}.log')
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


main()
