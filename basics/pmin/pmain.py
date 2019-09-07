#import pminimum as pmin
import pminimum_pass as pmin
import test_pmin as test

list_to_work_with = [4,5,6]
print(pmin.pminimum(list_to_work_with))

try:
    pmin.pminimum(list_to_work_with)
except:
    print("Exception risen")
else:
    print("No exception")

test.test_pminimum()