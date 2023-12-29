"""Utility functions for the project

This module contains utility functions for the project. It is used by the main script and the tests.

Functions:
get_logger: creates a logger object
ping_redis: pings the Redis server
check_file_arg: checks if the file argument is valid
check_dir_arg: checks if the directory argument is valid
check_workers_arg: checks if the workers argument is valid

Author:
Stefan Vulpe

Date:
2023/12/28
"""

import argparse
import logging
import os


def get_logger(name, log_file):
    """Creates a logger object

    Creates a logger object and adds a file handler and a stream handler.

    Args:
    name (str): logger name
    log_file (str): path to the log file

    Returns:
    logging.Logger: logger object
    """
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
    """Pings the Redis server

    Pings the Redis server and logs the result.

    Args:
    redis_conn (Redis): Redis connection object
    logger (logging.Logger): logger object

    Returns:
    None

    Exit codes:
    1: cannot connect to Redis
    """
    try:
        redis_conn.ping()
    except Exception as e:
        logger.error(f'Cannot connect to Redis server: {e}')
        exit(1)
    else:
        logger.info('Connected to Redis')


def check_file_arg(file_path):
    """Checks if the file argument is valid

    Checks if the file argument is valid. If the file does not exist, an error is raised.

    Args:
    file_path (str): path to the file

    Returns:
    str: path to the file

    Raises:
    argparse.ArgumentTypeError: if the file does not exist
    """
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f'File {file_path} does not exist')
    return file_path


def check_dir_arg(dir_path):
    """Checks if the directory argument is valid

    Checks if the directory argument is valid. If the directory does not exist, an error is raised.

    Args:
    dir_path (str): path to the directory

    Returns:
    str: path to the directory

    Raises:
    argparse.ArgumentTypeError: if the directory does not exist
    """
    if not os.path.isdir(dir_path):
        raise argparse.ArgumentTypeError(f'Output directory {dir_path} does not exist')
    return dir_path


def check_workers_arg(workers):
    """Checks if the workers argument is valid

    Checks if the workers argument is valid. If the workers argument is not an integer or is less than 1, an error is raised.

    Args:
    workers (str): number of workers

    Returns:
    int: number of workers

    Raises:
    argparse.ArgumentTypeError: if the workers argument is not an integer or is less than 1
    """
    try:
        workers = int(workers)
    except ValueError:
        raise argparse.ArgumentTypeError(f'Number of workers must be an integer')
    if workers < 1:
        raise argparse.ArgumentTypeError(f'Number of workers must be at least 1')
    return workers

