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


class Item:
    _id = 0
    food_list = ['pizza', 'burger', 'sandwich']
    beverage_list = ['mohito', 'limonad']
    starter_list = ['sezar', 'fasl']
    price = [20000, 21000, 50000]
    datetime = datetime.now()

    # fullname = input("(Please  Enter customer Name) :")
    # input2 = input("(Please Enter Category food ,starter, beverage) :")
    # if input2 == 'food'or 'starter'or 'beverage':
    #     print(price)
    # input3 = input("(Please Enter the desired item ) :")
    # if input3 in dict.keys(price):
    #     print('me')
    # item = input1.split(), input2.split(), input3.split()
    # print(item)
    #
    def __init__(self, uuid, name, price, food_list, beverage_list, datetime, item_type, starter_list, *args, **kwargs):
        self.uuid = self.generate_id()
        self.name = name
        self.food_list = food_list
        self.starter_list = starter_list
        self.beverage_list = beverage_list
        self.datetime = datetime.now()
        self.item_type = item_type
        self.price = price
        super().__init__(*args, **kwargs)

    @classmethod
    def sample(cls, uuid=uuid4(), name='pem', food_list='pizaa', starter_list='sezar', beverage_list='mohito',
               datetime=datetime, item_type='food_list', price=20000):
        return cls(uuid=uuid, name=name, food_list=food_list, starter_list=starter_list,
                   beverage_list=beverage_list, datetime=datetime, item_type=item_type, price=price)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id



