#import pminimum as pmin
import pminimum_pass as pmin
      
def test_pminimum():
    ''' TC1: Empty array; ER: error returned signalling empty attribute.
        TC2: All values are equal; ER: returns value
        TC3: [1000,999,998,...,1]; ER: 1
        TC4: [1,2,1,2,1,2]; ER: 1
        TC5: all values are negative; ER: returns negative minimum
        
        TBD:
        TC1: Empty array; ER: error returned signalling empty attribute.
        TC2: All values are equal; ER: returns value and [0,1,2,...,len-1] positions
        TC3: [1000,999,998,...,1]; ER: 1, [999]
        TC4: [1,2,1,2,1,2]; ER: 1, [0,2,4]
        TC5: all values are negative; ER: returns negative minimum
    '''
    test_pminimum_TC1()
    test_pminimum_TC2()
    test_pminimum_TC3()
    test_pminimum_TC4()
    test_pminimum_TC5()

def test_pminimum_TC1():
    try:
        if len(pmin.pminimum([])) > 0:
            print("TC1 failed.")
            return 1
    except ValueError:
        print("TC1 passed.")
        return 0
    except:
        print("TC1 failed, exception risen.")
        return 101
    else:
        print("TC1 failed.")
        return 1

def test_pminimum_TC2():
    try:
        arr = [1,1,1,1,1,1,1,1]
        if pmin.pminimum(arr) != 1:
            print("TC2 failed.")
            return 2
    except:
        print("TC2 exception.")
        return 102
    else:
        print("TC2 passed.")
        return 0
    
def test_pminimum_TC3():
    try:
        arr = range(1000,0,-1)
        if pmin.pminimum(arr) != 1:
            print("TC3 failed.")
            return 3
    except:
        print("TC3 exception.")
        return 103
    else:
        print("TC3 passed.")
        return 0

def test_pminimum_TC4():
    try:
        arr = [1,2,1,2,1,2]
        if pmin.pminimum(arr) != 1:
            print("TC4 failed.")
            return 4
    except:
        print("TC4 exception.")
        return 104
    else:
        print("TC4 passed.")
        return 0

def test_pminimum_TC5():
    try:
        arr = [-1,-2,-4,-6,-1000,-1,-3,-4,-8]
        if pmin.pminimum(arr) != -1000:
            print("TC5 failed.")
            return 5
    except:
        print("TC5 exception.")
        return 105
    else:
        print("TC5 passed.")
        return 0
