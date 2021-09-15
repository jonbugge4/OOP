class cellphone:
    
    def __init__(self, manu, model, retail):
        self.__manufact = manu
        self.__model_num = model
        self.__retail_price = retail

    def set_manufact(self,manu):
        self.__manufact = manu

    def set_model(self, model):
        self.__model_num = model

    def set_retail_price(self, retail_price):
        if retail_price < 0:
            print('Nice try...')
        else:
            self.__retail_price = retail

    def get_manufact(self):
        return self .__manufact

    def get_model(self):
        return self.__model_num

    def get_retail_price(self):
        return self.__retail_price



    
