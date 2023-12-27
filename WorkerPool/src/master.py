import argparse
import json
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
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='Path to the output directory, where the results will be saved')
    parser.add_argument('-q', '--queue', type=str, default='worker-pool-queue', help='Redis queue name')
    parser.add_argument('-w', '--workers', type=int, default=1, help='Number of workers to spawn')
    return parser.parse_args()


def read_input_data(file_path, logger):
    file = None
    try:
        file = open(file_path, 'r')
        return json.load(file)
    except FileNotFoundError as e:
        logger.error(f'File not found: {e}')
        exit(1)
    except PermissionError as e:
        logger.error(f'Permission error: {e}')
        exit(1)
    except IOError as e:
        logger.error(f'IO error: {e}')
        exit(1)
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        exit(1)
    finally:
        if file:
            file.close()


def populate_queue(redis_conn, queue_name, input_data, output_dir, logger):
    if redis_conn.exists(queue_name):
        logger.info(f'Queue {queue_name} already exists')
        logger.info('Deleting the queue')
        redis_conn.delete(queue_name)
        logger.info('Queue deleted')

    print('Do you want to create separate folders for each country? (y/n)')
    choice = input('Enter your choice: ')

    for country, sites in input_data.items():
        for link in sites.values():
            if choice == 'y':
                disk_location = f'{output_dir}\\{country}'
            elif choice == 'n':
                disk_location = f'\\{output_dir}'
            else:
                print('Invalid choice')
                exit(1)
            try:
                redis_conn.lpush(queue_name, json.dumps({'DiskLocation': disk_location, 'link': link}))
                redis_conn.expire(queue_name, 60 * 5)
                logger.info(f'Pushed {link} to {queue_name}')
            except Exception as e:
                logger.error(f'Cannot push to {queue_name}: {e}')


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

    logger.info(f'Path to file: {args.file}')
    logger.info(f'Path to output directory: {args.output}')
    logger.info(f'Queue name: {args.queue}')
    logger.info(f'Number of workers: {args.workers}')

    input_data = read_input_data(args.file, logger)

    populate_queue(redis_conn, args.queue, input_data, args.output, logger)

    logger.info('master end successfully')


if __name__ == '__main__':
    main()
