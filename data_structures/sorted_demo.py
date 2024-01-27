""" sorted() method """


demo_list = [2, -1, -2, 3, -3, 8, 6, 6, 1, 0]

print(sorted(demo_list)) # simple sorted()


def sorted_key(num):
    return num * num

print(sorted(demo_list, key=sorted_key)) # sorted with key
