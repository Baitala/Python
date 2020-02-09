my_list = ['asdf 1234 kdkdkd', 'fdsa 4321 kdkdkd']

a1 = 'asdf'
a2 = '1234'

for row in my_list:
    if a1 in row and a2 in row:
        print(row)