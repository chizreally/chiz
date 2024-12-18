#sum of inputs and all odd and even numbers

total = 0
even = 0
odd = 0

for x in range(1, 6):
    num = eval(input(f"Input a number and we will add it. \n Current Total: {total} \n"))
    total += num
    solve = num % 2
    if solve == 0:
        even += num
    elif solve >= 0:
        odd += num
    else:
        print("Invalid input.")
print(f"The sum of all numbers given by the user is {total}. \n Sum of all even numbers is {even}. \n Sum of all odd numbers is {odd}.")

