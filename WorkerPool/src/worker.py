import argparse
import json
import logging
import os

from dotenv import dotenv_values
from pywebcopy import save_webpage
from redis import Redis


def get_logger():
    logger = logging.getLogger(f'worker-{os.getpid()}')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")

    fh = logging.FileHandler(f'./logs/worker-{os.getpid()}.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


def parse_args():
    parser = argparse.ArgumentParser(prog='worker.py', description='Worker process for RQ workers')
    parser.add_argument('-q', '--queue', type=str, default='worker-pool-queue', help='Redis queue name')
    return parser.parse_args()


def process_job(job, logger):
    logger.info(f'Worker {os.getpid()} processing job: {job}')
    job_content = json.loads(job[1])
    output_dir = job_content['DiskLocation']
    page_url = f'https://www.{job_content['link'].lower()}'

    os.makedirs(output_dir, exist_ok=True)

    try:
        save_webpage(url=page_url, project_folder=output_dir, project_name=job_content['link'], open_in_browser=False,
                     bypass_robots=True)
    except Exception as e:
        logger.error(f'Unexpected error saving page {page_url}: {e}')

    logger.info(f'Worker {os.getpid()} finished processing job: {job}')


def work(redis_conn, queue_name, logger):
    while True:
        job = redis_conn.brpop(queue_name, 0)
        logger.info(f'Worker {os.getpid()} got job: {job}')
        process_job(job, logger)


def main():
    logger = get_logger()
    args = parse_args()

    logger.info(f'Worker {os.getpid()} started')

    if dotenv_values('.env') == {}:
        logger.error('No .env file found')
        exit(1)

    redis_conn = Redis(host=dotenv_values('.env')['REDIS_HOST'], port=dotenv_values('.env')['REDIS_PORT'],
                       decode_responses=True)

    work(redis_conn, args.queue, logger)

    logger.info(f'Worker {os.getpid()} finished')


if __name__ == '__main__':
    main()
