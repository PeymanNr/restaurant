# TODO-1: Add Table class here
# TODO-1: Add .sample() classmethod for Table which returns  an instance:
# for example:
class Table:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @classmethod

    def sample(cls, name, number):
        return cls(name='ali', number=10)
