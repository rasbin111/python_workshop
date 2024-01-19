def print_string(string_input):
    """this function simply prints given string on the screen
    >>> print_string("hello")
    hello
    >>> print_string("namaste")
    namaste
    """
    print(string_input)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
