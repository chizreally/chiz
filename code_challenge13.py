#adding inputs until the input is '0' while also using the 'while' statement

#setting the variable

running = True
total = 0

#main lines of code

print("Give a number to add up with other inputs, inputting '0' will terminate the loop.")

while running == True :
    num = eval(input("Enter a number: "))

    if num >= 1 or num == 1 :
        total += num
        print(f"\nTotal: {total}")
    elif num == 0 :
        print(f"The sum of all inputs is {total}")
        print("LOOP TERMINATED")
        break
        running = False
    else:
        print("Invalid input, try to enter '1' or a number more than '1'.")