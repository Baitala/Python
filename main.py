import nuber as n
import test_nuber
#user_input = int(input("Enter some number: "))
#print ("Flipped number is: ", n.flip_nuber(user_input))

tests = test_nuber.test_flip_number()
if tests == 0:
    print("Tests passed.")
elif tests < 100:
    print("Test case #",tests," FAILED.")
else:
    print ("Function crashed in TC # ", tests - 100)