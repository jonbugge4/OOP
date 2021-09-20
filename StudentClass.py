from datetime import date

class Students:
    def __init__(self, StudentID, StudentName, DateofBirth, classification):
        self.__student = StudentID
        self.__name = StudentName
        self.__dob = DateofBirth
        self.__classs = classification
        self.__age = 0 
        self.__registration = ''


    def get_age(self):
        return self.__age

    def get_registration(self):
        return self.__registration

    def register(self, classification):
        if self.__classification == 'Seniors':
            self.__registration == '11/1 = 11/3'
        elif self.__classification =='Juniors':
            self.__registration == '11/4 - 11/6'
        elif self.__classification == 'Sophomores':
            self.__registration == '11/7 - 11/9'
        elif self.__classification == 'Freshman':
            self.__registration == '11/10 - 11/12'
        else:
            self.__registration = 'calssification not found'

    def calc_age(self):
        today = date.today()
# split the string
        bday = self.__dob.split('/')
# call the third piece of the string (0,1,2)
        bday_year = int(bday[2])
        age = today.year - bday_year
        self.__age = age


      
        
        




    
