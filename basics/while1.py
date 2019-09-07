import functions_prototyping as fp

def printing_for_no_reason():
    key = input("Enter command: ")
    while key != "exit":
        print("You entered: ",key)
        key = input("Enter command: ")
        if key == "quit":
            break
    else:
        print("Program completed successfully.")

#printing_for_no_reason()

key = int(input("Enter number: "))
if fp.is_even_number(key):
    print(key, " is even number")
else:
    print(key, " is odd number")
    