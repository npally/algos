"""
Factorial algorithm with loop
"""

def fact(n):
    x = 1
    for i in range(n):
        x += i * x
    return x


"""
Factorial algorithm with recursion
"""

def recursive_fact(n):
    if n == 1:
        return n
    else:
        return n * recursive_fact(n-1)

