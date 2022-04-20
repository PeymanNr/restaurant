# TODO-1: Add Item class here
# TODO-1: Add .sample() classmethod for Item which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)

# TODO-2: Add item_id to the Item class, item_id should be auto incremental
# TODO-2: item_types should be one of (f, s or b) for Food, Starter or Beverage
# TODO-2: Change datetime attr to be assigned automatically in Item class
# TODO-2: Add jalali_datetime property to the Item class
# TODO-3: Add show_menu() classmethod to the Item class which will print all
#       items in the menu
# TODO-3: Add prompt() method to the Item class which will get proper dict for
#       creating each single item from user input and return data
from datetime import datetime
from uuid import uuid4

name = input("enter name eat :")

item_type = input("please entered Category s or f or b: ")
price = input("Please enter Price: ")
result = {'name': name, 'item_type': item_type, 'price': price}


class Item:
    _id = 0
    item_list =[]
    food_list = []
    beverage_list = []
    starter_list = []
    datetime = datetime.now()
    item_type = []

    def __init__(self, name, price, item_type, *args, **kwargs):
        self.uuid = self.generate_id()
        self.name = name
        self.uuid = uuid4()
        self.datetime = datetime.now()
        self.search_item()
        self.item_type = item_type
        self.price = price
        super().__init__(*args, **kwargs)

    def sample(cls, name='pem', item_type='f', price=20000):
        return cls(name=name,item_type=item_type, price=price)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    # @classmethod
    # def inputs(cls):

    def search_item(self):
        if item_type == 's':


