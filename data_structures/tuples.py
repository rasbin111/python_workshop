""" 
If you want to determine explicitly if a tuple (or any 
object) has a fixed value, you can use the hash built-in 
to create a fixed function like this
"""
def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tuple_one = (10, 'alpha', (20, 30))
tuple_two = (10, 'alpha', [20, 30])

print(fixed(tuple_one))
print(fixed(tuple_two))
        
