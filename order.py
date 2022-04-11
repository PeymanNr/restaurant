# TODO-1: Add Order model here
# TODO-1: Add .sample() classmethod for Order which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
# TODO-2: Replace all uuid attrs with uuid.uuid4() method and prevent class
# TODO-2: Add jalali_datetime property to the Order class
# TODO-2: uuid and datetime attrs should be assigned automatically
# TODO-2: Store a list of orders and a list for un_paid_orders
# TODO-2: Add set_bill method to the Order class which create proper Bill
#       instance according to the items in the order
# TODO-2: Add assign_table method to the Order class which assign table to the
#       client and change the table status
# TODO-2: Set I/O for in_out option in Order class

from uuid import uuid4
from finance import Bill
from saloon import Table


class Order:
    _id = 0

    def __init__(self, uuid, item_dict, in_out, bill, table, *args, **kwargs):
        self.uuid = self.generate_id()
        self.item_dict = item_dict
        self.in_out = in_out
        self.bill = Bill()
        self.table = Table()
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, uuid=uuid4(), item_dict='d', in_out='ddd', bill='cfhcfghf', table='dfgxdfg'):
        return cls(uuid=uuid, item_dict=item_dict, in_out=in_out, bill=bill, table=table)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id
