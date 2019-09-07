####################################
#### W R O N G !!!!!!!!!!!
#####################################
#checking out yield and generators

#def arithmetic(max):
#    '''Generates arithmetic progression from 0 to max
#    '''
#    for i in range(0,max+1,1):
#        yield i

def arithmetic(max):
    '''Generates arithmetic progression from 0 to max
    '''
    if max < 0:
        raise ValueError
    if max == 0:
        yield [0]

    assert max > 1000000, "Argument too big"
    i = 0
    while i < max:
        i += 1
        yield i

def ar_linear():
    i = 1
    yield i

    i += 2
    yield i

    i += 3
    yield i

def test_arithmetic():
    '''Tests arithmetic.
    TC1: next number is more than previous one.
    TC2: max = 0; ER: [0]
    TC3: max < 0; ER: exception.
    TC4: max > 1000000; ER: assertion "Argument too big".
    '''
    #test_arithmetic_TC1()
    test_arithmetic_TC2()
    test_arithmetic_TC3()
    if __debug__:
        test_arithmetic_TC4()


#def test_arithmetic_TC1():
#    '''TC1: next number is more than previous one.
#    '''
#    arr = arithmetic(100)
#    try:
#        curr_val_less = arr[0]
#        for i in range(1,101,1):
#            curr_val_more = arr[i];
#            if curr_val_less > curr_val_more:
#                print("TC1 failed.")
#                return 1
#            curr_val_less = curr_val_more
#    except:
#        print("Exception in TC1.")
#        return 101
#    else:
#        print("TC1 passed.")
#        return 0

def test_arithmetic_TC2():
    '''TC2: max = 0; ER: [0]
    '''
    try:
        if arithmetic(0) != [0]:
            print("TC2 failed.")
            return 2
    except:
        print("Excpetion in TC2.")
        return 102
    else:
        print("TC2 passed.")
        return 0

def test_arithmetic_TC3():
    '''max < 0; ER: exception.
    '''
    try:
        arithmetic(-1)
    except ValueError:
        print("TC3 passed.")
        return 0
    except:
        print("Exception in TC3.")
        return 103
    else:
        print("TC3 failed.")
        return 3

def test_arithmetic_TC4():
    '''max > 1000000; ER: assertion "Argument too big".
    '''
    print("'Assertion: Argument too big' means TC4 is passed")
    try:
        arithmetic(1000001)
    except AssertionError:
        print("TC4 passed.")
        return 0
    except:
        print("Exception in TC4.")
        return 104
    else:
        print("TC4 failed.")
        return 4



