import RetailClass as c
def main():
    create = 'Y'

    while create is 'Y':
        count = 0
#create an ItemNum object
        Item(count +1) = c.RetailItem.ItemNum
        c.description = input('Item Description: ')
        c.unit_inventory = input('Number of Units: ')
        c.unit_price = input('Price per unit: ')
        create = input('Would you like to add another item? (Y/N) ')
    else:
        open('RetailItem.txt', 'w')
        print(c.ItemNum)

        c.RetailItem.txt.close()

main()







        


