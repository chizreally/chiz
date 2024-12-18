#diamond kinda thing

for x in range(5, 0, -1):
    for y in range(1, x, +1):
        print(" ", end= " ")
    for z in range(6, x, -1):
        print("*", end= " ")
    for a in range(6, x, -1):
        print("*", end= " ")
    print()
for pa in range(1, 6):
    for pe in range(1, pa, +1):
        print(" ", end= " ")
    for pi in range(6, pa, -1):
        print("^", end= " ")
    for po in range(6, pa, -1):
        print("^", end= " ")
    print()
