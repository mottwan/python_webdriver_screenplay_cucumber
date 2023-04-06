from abc import ABC, abstractmethod


class Task(ABC):
    @abstractmethod
    def perform_as(self, actor):
        pass
