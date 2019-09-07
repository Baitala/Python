def flipflop(invalue):
    '''returns 'flip' if received flop
    returns 'flop' if received flip '''
    return 'flip' if invalue == 'flop' else 'flop' if invalue == 'flip' else ''

print(flipflop('flop'))
print(flipflop('flip'))
print(flipflop('sadf'))