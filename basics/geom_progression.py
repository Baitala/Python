def geom(start, stop, step):
    """range-like generator of geometry progression"""
    value = start
    while value < stop:
        value *= step
        yield value 

if __name__ == "__main__":
    for i in geom(2, 10000000, 2):
        print("Iterator =", i)

