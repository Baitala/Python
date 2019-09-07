#OOP take two

class Car:
    '''
    sdfasdfdsf
    '''
    type = "Man made mechanism"

    def __init__(self,fuel_type):
        if fuel_type == "diesel":
            #incapsulation
            self.__diesel = True
        else:
            self.__diesel = False

    def __setattr__(self, attr, value):
        if attr == 'field1':
                self.__dict__[attr] = value
        else:
                raise AttributeError

    def is_diesel(self):
        return self.__diesel

    def can_fly(self):
        return False

#inheritance
class Audi(Car):
    """
    asfsdafsda
    """
    def __init__(self,car_model):
        self.__model = car_model
    
    def what_is_model(self):
        return self.__model
    
    def is_diesel(self):
        return False

class Airplane:

    def can_fly(self):
        return True

def does_it_fly(mechanism):
    if mechanism.can_fly():
        print("It can fly")
    else:
        print("It can NOT fly")

