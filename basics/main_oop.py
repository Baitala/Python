import classes as c

my_obj1 = c.MyClass()
my_obj2 = c.MyClass()

my_obj1.say_hello()

for i in 1,2,3:
    my_obj2.set(i)
    my_obj2.get()
    print(my_obj2.number)

#####баловство
class EmptyClass:
    pass

empty_obj = EmptyClass()

empty_obj.field = "myvalue"

print(empty_obj.field)

del empty_obj.field

print(empty_obj.field)
###################
elev1 = c.Elevator()
elev2 = c.Elevator()
elev3 = c.Elevator()
elev4 = c.Elevator()

print(elev1.door_open)
elev1.closeDoors()
print(elev1.door_open)