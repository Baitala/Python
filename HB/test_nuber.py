import nuber
import sys

def test_flip_number():
    """
    TC1. One digit number. ER: The same value.
    TC2. Negative number. ER: Returns flipped number with minus.
    TC3. Zero. ER: Zero.
    TC4. Max digits input (1024). ER: Returns properly flipped number.
    TC5. Min digits input (-1024). ER: Returns properly flipped number.
    TC6. Input > 1024. ER: error.
    TC7. Input < -1024. ER: error.
    TC8. Input with the same digits. ER: returns itself.
    TC9. Input with zeros in the end. ER: returns value without leading zeros.
    TC10. Symetric number. ER: Returns itself.   
    """
    #TC1 
    try:
        if nuber.flip_nuber(5) != 5:
            return 1
    except:
        return 101
    
    #TC2
    try:
        if nuber.flip_nuber(-65) != -56:
            return 2
    except:
        return 102

    #TC3
    try:
        if nuber.flip_nuber(0) != 0:
            return 3
    except:
        return 103

    #TC8
    try:
        if nuber.flip_nuber(5555) != 5555:
            return 8
    except:
        return 108

    #TC9
    try:
        if nuber.flip_nuber(1000) != 1:
            return 9
    except:
        return 109

    #TC10
    try:
        if nuber.flip_nuber(32123) != 32123:
            return 10
    except:
        return 110
    
    #Tests passed
    return 0