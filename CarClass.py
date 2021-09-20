class CarClass:

    def __init__(self, year_model, car_make, car_speed):
        self.__year = year_model
        self.__make = car_make
        self.__speed = car_speed
        car_speed = 0

    def set_year(self, year_model):
        self.__year = year_model

    def set_make(self, car_make):
        self.__make = car_make
    
    def set_speed(self, car_speed):
        self.__speed = car_speed

    def accelerate(self, car_speed):
        self.__accel = car_speed + 5

    def brake(self, car_speed):
        self.__brak = car_speed - 5

    def get_accelerate(self):
        return self.__accel 

    def get_brake(self):
        return self.__brak

    def get_make(self):
        return self.__make

    def get_year_model(self):
        return self.__year

    def get_speed(self):
        return self.__speed