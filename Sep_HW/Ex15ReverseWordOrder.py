# Write a program (using functions!) that asks the user for a long string 
# containing multiple words. Print back to the user the same string, except 
# with the words in backwards order. For example, say I type the string:
#   My name is Michele
# Then I would see the string:
#   Michele is name My
# shown back to me.

def reverse_string(user_string):
    '''The function took a string and reverse it by words and returns a
    string'''
    user_list = user_string.split(" ")
    length = len(user_list)
    reverse_list = []
    iterator = length -1
    while iterator >= 0:
        reverse_list.append(user_list[iterator])
        iterator -= 1
    rev_string = " ".join(reverse_list)
    return rev_string



if __name__ == "__main__":
    a = "My name is Michele"
    print("Pass1" if reverse_string(a) == "Michele is name My" else "Error1")
    print("Pass2" if reverse_string("Lazy fox is jumping over a") == "a over jumping is fox Lazy" else "Error2")