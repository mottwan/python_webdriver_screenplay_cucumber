from questions.question import Question
from tasks.task import Task


class Actor:
    def __init__(self, name):
        self.name = name
        self.abilities = {}

    @classmethod
    def named(cls, name):
        return cls(name)

    def can(self, ability):
        self.abilities[ability.__class__] = ability
        return self

    def attempts_to(self, *tasks: Task):
        for task in tasks:
            task.perform_as(self)

    def should(self, question: Question):
        return question.answered_by(self)

    def ability_to(self, ability_type):
        return self.abilities.get(ability_type)
