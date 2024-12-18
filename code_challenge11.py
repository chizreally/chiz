
#diamornd

for x in range(5, 0, -1):
    for y in range(1, x, +1):
        print(" ", end= " ")
    for z in range(5, x, -1):
        print("*", end= " ")
    for a in range(4, x, -1):
        print("*", end= " ")
    print()
for m in range(1, 6):
    print(" ", end= " ")
    for n in range(1, m, +1):
        print(" ", end= " ")
    for b in range(4, m, -1):
        print("*", end= " ")
    for v in range(3, m, -1):
        print("*", end= " ")
    print()
    