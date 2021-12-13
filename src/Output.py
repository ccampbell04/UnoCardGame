from abc import ABC, abstractmethod


class Output(ABC):
    def getString(self, message):
        pass
