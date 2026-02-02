"""
# 1️⃣ Loop + range() (Control সহ loop)

for u in range(5):
    print(u)


for i in range(2, 15, 2):
    print(i)



# 2️⃣ Loop + enumerate() (Index + Value)

name = "Style"

for index, char in enumerate(name):
    print(index, char)


# 3️⃣ Loop + zip() (Multiple iterable)
a = "abc"
b = "123"
c = "!@#"

for x, y, z in zip(a, b, c):
    print(x, y, z)

# Neasted Loop
for i in range(3):
    for j in range(4):
        print(f"{i} : {j}")


# 6️⃣ Loop + break, continue

# break → loop থামিয়ে দেয়
for i in range(10):
    if i == 5:
        break
    print(i)


# continue → skip করে next loop
for i in range(5):
    if i == 2:
        continue
    print(i)


# 7️⃣ Loop + else (Rare but powerful)
for i in range(5):
    print(i)
else:
    print("Loop finished")


# squares = [x*x for x in range(5)]
# print(squares)

squares=[]

for x in range(5):
    squares.append(x*x)

print(squares)
"""

