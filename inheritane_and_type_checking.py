"""Polymorphism in Python.

1. An example on how to use polymorphism in Python using @classmethod.
2. An example on how to use static type checking
mypy <file_name.py>
3. How to create abstract classes in Python
"""

from __future__ import annotations
import os
import random
from threading import Thread
from typing import List, Iterator, TypedDict, Type, Iterable
from abc import ABCMeta, abstractmethod


TEMP_DIR = r"d:\temp\test_inputs"


class Config(TypedDict):
    data_dir: str
    number_of_files: int


class GenericInputData(metaclass=ABCMeta):
    @abstractmethod
    def read(self) -> str:
        ...

    @classmethod
    @abstractmethod
    def generate_inputs(cls, config: Config) -> Iterator[PathInputData]:
        ...


class PathInputData(GenericInputData):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path

    def read(self) -> str:
        with open(self.path) as f:
            return f.read()

    @classmethod
    def generate_inputs(cls, config: Config) -> Iterator[PathInputData]:
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(metaclass=ABCMeta):
    def __init__(self, input_data: PathInputData) -> None:
        self.input_data = input_data
        self.result = 0

    @abstractmethod
    def map(self) -> None:
        ...

    @abstractmethod
    def reduce(self, other: GenericWorker) -> None:
        ...

    @classmethod
    def create_workers(
        cls, input_class: Type[PathInputData], config: Config
    ) -> List[GenericWorker]:
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self) -> None:
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other: GenericWorker) -> None:
        self.result += other.result


def generate_inputs(data_dir: str) -> Iterator[PathInputData]:
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def execute(workers: Iterable[GenericWorker]) -> int:
    """Puts each worker on separate thread. Performs calculation
    and aggregation/reduce on all of them
    """

    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(
    worker_class: Type[LineCountWorker],
    input_class: Type[PathInputData],
    config: Config,
) -> int:
    """Creates thread workers for each file and performs execute on all of them."""

    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


def write_test_files(config: Config) -> None:
    """Creates test files for example in tmpdir."""

    os.makedirs(config["data_dir"], exist_ok=True)
    for i in range(config["number_of_files"]):
        with open(os.path.join(config["data_dir"], str(i)), "w") as f:
            f.write("\n" * random.randint(0, 100))


config = Config(data_dir=TEMP_DIR, number_of_files=100)
write_test_files(config)

result = mapreduce(LineCountWorker, PathInputData, config)
print(f"There are {result} lines")
