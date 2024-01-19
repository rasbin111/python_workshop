import re
import os

dummy_string = "Glory Glory manchester united"

first_search = re.findall("^G.+?y", dummy_string)


print(dummy_string)
print(first_search)

