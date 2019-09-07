def pminimum(numbers):
    ''' From array of numbers returns minimum value, 
        TBD: and list of positions when it appears,
        single value or more if more than one minimum. :TBD
    '''
    if len(numbers) == 0:
        raise ValueError
    min_value = numbers[0]
    for i in range(1,len(numbers),1):
        current_value = numbers[i]
        if current_value < min_value:
            min_value = current_value
    return min_value
  