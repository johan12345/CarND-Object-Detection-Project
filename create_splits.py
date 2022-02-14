import argparse
import glob
import os
import random
from typing import List

import numpy as np

from utils import get_module_logger

from pathlib import Path

val_pct = 0.2
test_pct = 0.2


def split(source: Path, destination: Path):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    destination.mkdir(exist_ok=True)
    train_dir = destination / "train"
    val_dir = destination / "val"
    test_dir = destination / "test"

    for path in train_dir, val_dir, test_dir:
        path.mkdir(exist_ok=True)
        clean_dir(path)  # make sure that it is empty

    source_files = [f for f in source.iterdir() if f.is_file() and f.suffix == '.tfrecord']
    random.shuffle(source_files)

    n_val = int(val_pct * len(source_files))
    n_test = int(test_pct * len(source_files))

    print(f"{len(source_files) - n_val - n_test} files in training set")
    print(f"{n_val} files in validation set")
    print(f"{n_test} files in test set")

    val_files = source_files[0:n_val]
    test_files = source_files[n_val:n_val + n_test]
    train_files = source_files[n_val + n_test:]

    symlink_files(val_files, val_dir)
    symlink_files(test_files, test_dir)
    symlink_files(train_files, train_dir)


def clean_dir(path: Path):
    """
    Deletes all files in a directory (note that it does not delete subdirectories)
    """
    for f in path.iterdir():
        if f.is_file() or f.is_symlink():
            f.unlink()


def symlink_files(files: List[Path], destination: Path):
    """
    Symlink given files into a destination directory
    """
    for file in files:
        dest = (destination / file.name)
        dest.symlink_to(file.absolute())



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True, type=Path,
                        help='source data directory')
    parser.add_argument('--destination', required=True, type=Path,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)