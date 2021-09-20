import CarClass as cc

def main():
    car = cc.CarClass(2002, 'Chevy', 0)
    

    for counter in range(1,5):
        car.accelerate()
        car.get_speed()
        print('The car is traveling at ',car.get_speed(), 'miles per hour')
        
    
    for counter in range(1,5):
        car.brake()
        car.get_speed()
        print('The car is traveling at ',car.get_speed(), 'miles per hour')

main()
