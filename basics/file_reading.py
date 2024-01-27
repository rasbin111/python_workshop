from pathlib import Path


path = Path("pi_digits.txt")

contents = path.read_text()
lines = contents.splitlines()
print(lines)

with open("pi_digits_copy.txt", "w") as f:
    for line in lines:
        f.write(line)


