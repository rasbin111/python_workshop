

"""
# without the walrus operator
n = 10
if n > 5:
    print(n)

# with the walrus operator
if (n := 10) > 5:
    print(n)
"""

"""
# without the walrus operator
n = 0
while n < 5:
    print(n)
    n += 1

# with the walrus operator
n = -1
while (n := n + 1) < 5:
    print(n)
"""

candidates = ["prachanda", "oli", "sherey"]
prompt = "Choose your fav leader: "

while (choice := input(prompt)) not in candidates:
    print(f"Sorry, {choice} is not a valid candidate")
print(f"you chose {choice}")
