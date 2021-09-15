import CellphoneClass

def main():
    manufact = input('Enter Phone Manufacturer here, fool: ')
    model_num = input('Enter your Phone Model here: ')
    retail_price = input('Enter your phone Price here: ')

    Iphone = CellphoneClass.cellphone(manufact, model_num, retail_price)

    print('Phone Manufacturer: ', Iphone.get_manufact())
    print('Model number: ', Iphone.get_model())
    print('Retail Price: ', Iphone.get_retail_price())

    Android = CellphoneClass.cellphone(manufact, model_num, retail_price)

    print('Phone Manufacturer: ', Android.get_manufact())
    print('Model number: ', Android.get_model())
    print('Retail Price: ', Android.get_retail_price())






main()
