#create class
class RetailItem:

#start __init__ with three attributes accounted for
    def __init__(self, description, unit_inventory, unit_price):
        self.__desc = description
        self.__units = unit_inventory
        self.__price = unit_price

# set item description for the item
    def set_description (self, description):
        self.__desc = description
# set number of units for the item
    def set_units (self, unit_inventory):
        self.__units = unit_inventory

# set the price per unit
    def set_price (self, unit_price):
        self.__price = unit_price

# return the description per item
    def get_description (self):
        return self.__desc

# return the units per item
    def get_units (self):
        return self.__units

# return the price per item
    def get_price (self):
        return self.__price



