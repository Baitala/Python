# def gen_bin(M, prefix=""):
#     if M ==0:
#         print(prefix)
#         return
#     for digin in "0", "1":
#         gen_bin (M-1, prefix+digin)
    


# # gen_bin(5)




# def generate_number(N:int, M:int, prefix=None):
#     ''''''
#     prefix = prefix or []
#     if M == 0:
#         print(prefix)
#         return
#     for digit in range(N):
#         prefix.append(digit)
#         generate_number(N, M-1, prefix)
#         prefix.pop()


# # generate_number(4, 3)
def find(number, A):
    '''Searches for number in A and returns Trus, if it is present and False if it 
    is not present'''
    for x in A:
        if number == x:
            return True
    return False


def generate_permutations(N:int, M:int=-1, prefix=None):
    '''The function generates N number is M positions, begins on prefix'''
    M = N if M != -1 else M # by default N numbers in N positions
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=", ")
        return
    for number in range (1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(3)