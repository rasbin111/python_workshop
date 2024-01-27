from itertools import compress

data = range(10)

odd_selector = [0, 1] * 10


odd_numbers = [odd_num for odd_num in compress(data, odd_selector)]
print(odd_numbers)

even_selector = [1, 0] * 5
even_numbers = [even_num for even_num in compress(data, even_selector)]
print(even_numbers)
