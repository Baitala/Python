import car
MyCar = car.Car(10, "Petro's car")
print ("My current speed is", MyCar.velocity)

MyCar.move_forward(5)

print ("My current speed is", MyCar.velocity)

print ("My current direction is", MyCar.direction)

MyCar.turn_left(15)
print ("My current direction is", MyCar.direction)

MyCar.turn_right(30)
print ("My current direction is", MyCar.direction)


MyCar.stop()
print ("My current speed is", MyCar.velocity)


Eugen_Car = car.Car(0, "Eugen's car")
print ("Eugen's car direction is", Eugen_Car.direction)

print("Foo =", MyCar.Foo, Eugen_Car.Foo)
car.Car.Foo = "B"
print("Foo =", MyCar.Foo, Eugen_Car.Foo)

del MyCar
while True:
    pass