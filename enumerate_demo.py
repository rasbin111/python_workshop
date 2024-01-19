footballers = ["Ronaldo", "Messi", "Neymar"]

""" enuemerate() method can be useful if we want index while using for loop"""
# enumerate(iterable, start=value), where start=value is optional and defaults to 0
for index, value in enumerate(footballers, start=0):
    print(f"Index: {index}", end=" ")
    print(f"Value: {value}")
