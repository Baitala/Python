def pmax(numbers:int):
    '''
    Gets list of numbers, returns maximum value, it's index;
    If more than one maximum, returns first entry of it.
    '''
    maximum = numbers[0]
    maximum_index = 0
    for i in range(1,len(numbers),1):
        current_num = numbers[i]
        if maximum < current_num:
            maximum = current_num
            maximum_index = i
    return maximum, maximum_index

def test_pmax():
    '''
        TC1: empty list; ER: error returned
        TC2: all values are equal; ER: value, 0 returned
        TC3: 
    '''
        