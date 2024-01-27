""" generator expressions """

symbols = "abc"
unicode_values = tuple((ord(symbol) for symbol in symbols))
print(unicode_values)
print(type(unicode_values))

