"""Master process for RQ workers

Usage:
python master.py -f <path_to_file> -o <path_to_output_directory> [-w <number_of_workers>] [-q <queue_name>]

Arguments:
-f, --file: path to the json file with top sites
-o, --output: path to the output directory, where the results will be saved
-w, --workers: number of workers to spawn
-q, --queue: Redis queue name

Exit codes:
1: file not found
1: permission error
1: IO error
1: unexpected error
1: no .env file found
1: queue already exists
1: cannot delete queue
1: cannot push to queue
1: cannot spawn worker

Example:
python master.py -f ./data/top_sites.json -o ./output -w 1 -q worker-pool-queue

Author:
Stefan Vulpe

Date:
2023/12/28
"""

import argparse
import json
import subprocess

from dotenv import dotenv_values
from redis import Redis

from src.utils.utils import get_logger, ping_redis, check_file_arg, check_dir_arg, check_workers_arg


def parse_args():
    """Parse command line arguments

    Parse command line arguments and return the parsed arguments.

    Returns:
    argparse.Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(prog='master.py', description='Master process for RQ workers')
    parser.add_argument('-f', '--file', type=check_file_arg, required=True, help='Path to the json file with top sites')
    parser.add_argument('-o', '--output', type=check_dir_arg, required=True,
                        help='Path to the output directory, where the results will be saved')
    parser.add_argument('-w', '--workers', type=check_workers_arg, default=1, help='Number of workers to spawn')
    parser.add_argument('-q', '--queue', type=str, default='worker-pool-queue', help='Redis queue name')
    return parser.parse_args()


def read_input_data(file_path, logger):
    """Reads the input data from a json file

    Reads the input data from a json file and returns it.

    Args:
    file_path (str): path to the json file
    logger (logging.Logger): logger object

    Returns:
    dict: input data

    Exit codes:
    1: file not found
    1: permission error
    1: IO error
    1: unexpected error
    """
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
    """Populates the queue with the input data

    Populates the queue with the input data. If the queue already exists, it is deleted and recreated.

    Args:
    redis_conn (redis.Redis): redis connection object
    queue_name (str): name of the queue
    input_data (dict): input data
    output_dir (str): path to the output directory
    logger (logging.Logger): logger object

    Exit codes:
    1: queue already exists
    1: cannot delete queue
    1: cannot push to queue
    1: unexpected error
    """
    if redis_conn.exists(queue_name):
        logger.info(f'Queue {queue_name} already exists')
        logger.info('Deleting the queue')
        redis_conn.delete(queue_name)
        logger.info('Queue deleted')

    for country, sites in input_data.items():
        for link in sites.values():
            disk_location = f'{output_dir}\\{country}'
            try:
                redis_conn.rpush(queue_name, json.dumps({'DiskLocation': disk_location, 'link': link}))
                redis_conn.expire(queue_name, 60 * 60)
                logger.info(f'Pushed {link} to {queue_name}')
            except Exception as e:
                logger.error(f'Cannot push to {queue_name}: {e}')


def spawn_workers(nr_of_workers, queue_name, logger):
    """Spawns the workers

    Spawns the workers and waits for them to finish.

    Args:
    nr_of_workers (int): number of workers to spawn
    queue_name (str): name of the queue
    logger (logging.Logger): logger object

    Exit codes:
    1: cannot spawn worker
    """
    logger.info(f'Spawning {nr_of_workers} workers')
    processes = []
    for i in range(nr_of_workers):
        logger.info(f'Spawning worker {i}')
        try:
            processes.append(subprocess.Popen(['python', './src/main/worker.py', '-q', queue_name]))
        except Exception as e:
            logger.error(f'Cannot spawn worker: {e}')

    for process in processes:
        process.wait()


def main():
    """Main function

    Main function of the master process. It parses the command line arguments, reads the input data from a json file,
    populates the queue with the input data and spawns the workers.

    Exit codes:
    1: no .env file found
    """
    logger = get_logger('master', './static/logs/master.log')
    args = parse_args()

    logger.info('master start')

    if dotenv_values('.env') == {}:
        logger.error('No .env file found')
        exit(1)

    redis_conn = Redis(host=dotenv_values('.env')['REDIS_HOST'], port=dotenv_values('.env')['REDIS_PORT'],
                       decode_responses=True)

    ping_redis(redis_conn, logger)

    logger.info(f'Path to file: {args.file}')
    logger.info(f'Path to output directory: {args.output}')
    logger.info(f'Queue name: {args.queue}')
    logger.info(f'Number of workers: {args.workers}')

    input_data = read_input_data(args.file, logger)

    populate_queue(redis_conn, args.queue, input_data, args.output, logger)

    spawn_workers(args.workers, args.queue, logger)

    logger.info('master end successfully')


if __name__ == '__main__':
    main()
