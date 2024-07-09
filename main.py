from abc import ABC, abstractmethod
from typing import Protocol


class Stream(Protocol):

    def read(self):
        pass


class A(Stream):
    pass


A()

