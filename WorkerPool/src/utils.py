import argparse
import logging
import os


def get_logger(name, log_file):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")

    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


def ping_redis(redis_conn, logger):
    try:
        redis_conn.ping()
    except Exception as e:
        logger.error(f'Cannot connect to Redis server: {e}')
        exit(1)
    else:
        logger.info('Connected to Redis')


def check_file_arg(file_path):
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f'File {file_path} does not exist')
    return file_path


def check_dir_arg(dir_path):
    if not os.path.isdir(dir_path):
        raise argparse.ArgumentTypeError(f'Output directory {dir_path} does not exist')
    return dir_path


def check_workers_arg(workers):
    try:
        workers = int(workers)
    except ValueError:
        raise argparse.ArgumentTypeError(f'Number of workers must be an integer')
    if workers < 1:
        raise argparse.ArgumentTypeError(f'Number of workers must be at least 1')
    return workers

