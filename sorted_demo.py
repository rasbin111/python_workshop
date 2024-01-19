""" sorted() method """

demo_list = [2, -1, -2, 3, -3, 8, 6, 6, 1, 0]


def sorted_key(num):
    return num * num


print(sorted(demo_list, key=sorted_key))
