import os

class ReadWriteToFile:
    '''Use RW to file'''
    def __init__(self):
        my_file = open("super_file.txt", "w")
        
        # my_file = open("super_file.txt", "a")
        my_file.write("Lazy fox is jumping over a text, text, text!")
        my_file.close()
        my_file = open("super_file.txt", "r")
        print(my_file.read())

# first_file = ReadWriteToFile()

def does_file_exist_with_try():
    '''Defines if super_file.txt exists and print "File exitsts" in case if it
    exists and "File doesn't exist" if it doesn't; try realization.'''
    try:
        f = open("super_file.txt")
        # Do something with the file
    except IOError:
        print("File doesn't exist")
    else:
        print("File exists")
        f.close()
        
does_file_exist_with_try()

def does_file_exist_with_os():
    '''Defines if super_file.txt exists and print "File exitsts" in case if it
    exists and "File doesn't exist" if it doesn't; OS realization.'''
    if os.path.isfile('super_file.txt'):
        print ("File exists")
    else:
        print ("File doesn't exist")

does_file_exist_with_os()