#flip number sequence

def flip_nuber(number):
    reversed_str = ""
    str_num = str(number)
    for position in range(len(str_num)-1, -1, -1):
         reversed_str += str_num[position]
    return int(reversed_str)


#    if reversed_str.count



