from Ex10ListOverlapComprehensions import list_common
from Ex10ListOverlapComprehensions import custom_list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# print(list_common(a,b))



list1 = custom_list(a)
list2 = custom_list(b)
print(list1 % list2)