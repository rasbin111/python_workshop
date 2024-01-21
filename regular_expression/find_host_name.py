import re

search_string = "From admin.frontend@rgt.com.np Sat Jan 5 09:14:14 2023"

host_name = re.findall(r'@(\S+)\s',search_string)

host_name_second_way = re.findall(r'@([^ ]*)', search_string)

print(host_name)
print(host_name_second_way)

