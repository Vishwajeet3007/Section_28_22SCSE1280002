from itertools import permutations
def allPermutations(string):

    # Using itertools.permutations
    permut = permutations(string)
    for p in permut:
        print("".join(p))
# def allPermutations(string,answer=''):

#     # Using Recursion
#     if len(string) == 0:
#         print(answer)
#         return
#     for i in range(len(string)):
#         ch = string[i]
#         left_substr = string[:i]
#         right_substr = string[i+1:]
#         rest = left_substr + right_substr
#         allPermutations(rest,answer + ch)
        
    


input_str = "abc"
allPermutations(input_str)