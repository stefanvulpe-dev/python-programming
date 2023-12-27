import argparse
import logging

from dotenv import dotenv_values
from redis import Redis


def get_logger():
    logger = logging.getLogger('master')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")

    fh = logging.FileHandler('./logs/master.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


def parse_args():
    parser = argparse.ArgumentParser(prog='master.py', description='Master process for RQ workers')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the json file with top sites')
    parser.add_argument('-q', '--queue', type=str, default='worker-pool-queue', help='Redis queue name')
    parser.add_argument('-w', '--workers', type=int, default=1, help='Number of workers to spawn')
    return parser.parse_args()


def main():
    logger = get_logger()
    args = parse_args()

    logger.info('master start')

    if dotenv_values('.env') == {}:
        logger.error('No .env file found')
        exit(1)

    redis_conn = Redis(host=dotenv_values('.env')['REDIS_HOST'], port=dotenv_values('.env')['REDIS_PORT'],
                       decode_responses=True)

    try:
        redis_conn.ping()
    except Exception as e:
        logger.error(f'Cannot connect to Redis server: {e}')
        exit(1)
    else:
        logger.info('Connected to Redis')

    logger.info(f'Number of workers: {args.workers}')
    logger.info(f'Queue name: {args.queue}')
    logger.info(f'Path to file: {args.file}')

    logger.info('master end')


if __name__ == '__main__':
    main()
