"""
$ python -m cProfile <python_file>
"""

def sum_odd_upto_n(n):
    sum = 0
    for i in range(1, n, 2):
        sum += i

def is_odd(num):
    if num % 2 == 0:
        return True

sum_odd_upto_n(100000)


