from math import inf

def true_divide(first, second):

    if second == 0:
        return inf
    else:
        return first / second

result3 = true_divide(49, 7)
print(result3)
result4 = true_divide(15, 0)
print(result4)