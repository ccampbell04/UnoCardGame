from abc import ABC, abstractmethod


class Output(ABC):
    def display(self, message):
        pass
