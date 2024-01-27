def unicode_values(symbols):
    codes = [ord(symbol) for symbol in symbols]
    print(codes)

# unicode_values("abc")
# unicode_values("ABC")

def cartesian_product(rows, columns):
    cp = [(row, column) for row in rows for column in columns]
    print(cp)

# cartesian_product(["black", "white"], ["S", "M", "L"])





