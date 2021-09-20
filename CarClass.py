class CarClass:

    def __init__(self, year_model, car_make, car_speed):
        self.__year = year_model
        self.__make = car_make
        self.__speed = car_speed
        

    def set_year(self, year_model):
        self.__year = year_model

    def set_make(self, car_make):
        self.__make = car_make
    
    def set_speed(self, car_speed):
        self.__speed = car_speed

    def accelerate(self):
        self.__speed += 5 

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed