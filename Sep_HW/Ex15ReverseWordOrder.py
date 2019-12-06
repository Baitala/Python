# Write a program (using functions!) that asks the user for a long string 
# containing multiple words. Print back to the user the same string, except 
# with the words in backwards order. For example, say I type the string:

#   My name is Michele

# Then I would see the string:

#   Michele is name My

# shown back to me.

def reverse_string(user_string):
    user_list = user_string.split(" ")
    length = len(user_list)
    return length


a = "My name is Michele"
print(reverse_string(a))

# if __name__ == "__main__":
#     a = "My name is Michele"
#     # b = "Michele is name My"
#     print("Pass1" if reverse_string(a) == "Michele is name My" else "Error1")