from abc import ABC, abstractmethod


class Question(ABC):
    @abstractmethod
    def answered_by(self, actor):
        pass
