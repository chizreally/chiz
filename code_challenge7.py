# BSIT-1B Grocery Store

name = input("Enter your name:     ")
age = eval(input("Enter your age:     "))

print(f"Welcome, {name}, age {age}.")

# Item
porkribs = 2100
porkribstax = 2100 * 0.123
porkribfinal = porkribstax + porkribs

grocery = input("Did you purchase a grocery today? Y or N")
grocery.lower()

if grocery == "y" :
    what = input("What did you purchase?")

    if what == "pork ribs" :
        print("Item Price: 2100")
        print(f"Tax: {porkribstax} ")
        print(f"Final Price: {porkribfinal}")

        payment = eval(input("How much would you like to pay?"))

        if payment >= porkribfinal or payment == porkribfinal :

            result = round(payment - porkribfinal)

            print(f"Your change is {result}. Thank you for shopping!")
        
        else:
            print("Insufficient balance.")
elif grocery == "n" :
    print("nugagawin?")
else:
    print("Invalid response.")