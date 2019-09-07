from oop import *

Eugenes_car = Car("diesel")
#print(Eugenes_car.__diesel)
print(Eugenes_car.is_diesel())
print(Eugenes_car.__class__.type)

Eugenes_Audi = Audi("T")
print(Eugenes_Audi.__class__.type)
print(Eugenes_Audi.what_is_model())
print(Eugenes_Audi.is_diesel())

#polymorphism
does_it_fly(Eugenes_Audi)

#Eugenes_car.newfield = 5