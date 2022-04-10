# TODO-1: Add Bill class here
# TODO-1: Add Payment class here
# TODO-1: Add .sample() classmethod for Bill and Payment which returns

# an instance:
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
#       to get from input
# TODO-2: Change datetime attr to be assigned automatically in Payment class
# TODO-2: Add jalali_datetime property to the Payment class
# TODO-3: Set valid Payment instance for payment attr in Bill instance
# TODO-3: Add show_unpaid() classmethod to the Bill class which will return a
#       list of all unpaid bills, (Implementation is up to you)
# TODO-3: Add show_paid() classmethod to the Bill as show_unpaid() method
# TODO-3: Add paid_list() classmethod to the Payment class which will just
#       return a list of payments with True `is_paid` flag.
# TODO-3: Add pay() method to the Payment class which set is_paid flag True
# TODO-3: Add total_paid() classmethod to the Payment class which return an int
#       of total paid Payments


from abc import ABC, abstractmethod
from datetime import datetime
from menu import Item


is_paid = ('Yes', 'No')
datetime = datetime.now()
payment_type = ('cash', 'card')


class Payment(Item):
    # _id = 0

    def __init__(self, payment_type, is_paid, datetime, price, *args, **kwargs):
        self.payment_type = payment_type
        self.is_paid = is_paid
        self.datetime = datetime
        self.price = price
        self.uuid = self.generate_id()
        super().__init__(*args, **kwargs)

    @classmethod
    def sample3(cls, price, payment_type, is_paid, datetime):
        return cls(price, payment_type, is_paid, datetime)

    # @classmethod
    # def generate_id(cls):
    #     cls._id += 1
    #     return cls._id


class Bill(ABC):
    _id = 0
    def __init__(self,total_price,*args, **kwargs):
        self.total_price = total_price
        self.uuid = self.generate_id()
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id