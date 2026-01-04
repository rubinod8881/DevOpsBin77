row=6
for i in range(row):
    for j in range(row-i-1):
        print(" ", end="")
    for j in range(2*i+1):
            print("*", end="")
    print()
row = 6
for i in range(row, 0, -1):
    for j in range(row - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

row = 10
# Top Half (Pyramid)

for i in range(row):

    print(row * (row-i-1) + "*" * (2*i+1))
# Bottom Half (Inverted Pyramid)

for i in range(row - 2, -1, -1):

    print(" " * (row - i - 1) + "*" * (2 * i + 1))
