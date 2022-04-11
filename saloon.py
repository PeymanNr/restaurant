# TODO-1: Add Table class here
# TODO-1: Add .sample() classmethod for Table which returns  an instance:
# for example:
from unittest.case import _id
from uuid import uuid4


class Table:

    _id = 0
    table_list = list

    def __init__(self, uuid, capacity, number, reserved, is_available, *args, **kwargs):
        self.capacity = capacity
        self.uuid = self.generate_id()
        self.reserved = reserved
        self.number = number
        self.is_available = is_available
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, uuid=uuid4, capacity='dfd', number=65695496, reserved='d', is_available='nof'):
        return cls(uuid=uuid, capacity=capacity, number=number, reserved=reserved, is_available=is_available)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id
