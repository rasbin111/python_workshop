import re

search_string = "From rasbingodarthapa@gmail.com 10:20 pm, Dec 14, 2023"

result = re.findall(r'^From (\S+@\S+)', search_string)

print(result)


