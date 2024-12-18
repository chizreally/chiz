#Misc
import os
running = True

#Functions
def First():
    os.system('cls')
    name = input("What is your name? ")
    age = eval(input("How old are you now? "))
    NameAge(name, age)

def NameAge(name, age):
    """This function will ask for the user's name and their age, and will determine what are they in terms of their age."""
    if age <= 18:
        os.system('cls')
        print(f"Greetings {name}! You are currently {age} years old, a minor.")
        x = input("\nEnter any input to continue.")
        Colora()
    elif age >= 18 and age <= 100:
        os.system('cls')
        print(f"Greetings {name}! You are currently {age} years old, an adult.")
        x = input("\nEnter any input to continue.")
        Colora()
    elif age >= 100:
        os.system('cls')
        print(f"Greetings {name}! You are currently {age} years old, more than a hundred years old!?")
        x = input("\nEnter any input to continue.")
        Colora()
    else:
        os.system('cls')
        print("Something is not right!")

def Colora():
    """This will ask for any amount of colors """
    os.system('cls')
    print("Give me a color to add to your list! Once you're done, input 'x'.")
    lista = []
    colorlist = [
        "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", 
        "black", "white", "gray", "cyan", "magenta", "lime", "indigo", "violet",
        "gold", "silver", "beige", "turquoise", "teal", "navy", "maroon", "orchid",
        "salmon", "peach", "lavender", "chartreuse", "crimson", "sienna", "azure",
        "amber", "periwinkle", "mint", "plum", "honeydew", "ivory"
    ]
    colormode = True
    while colormode == True:
        color = input("Enter a color: ")
        if color in colorlist:
            lista.append(color)
        elif color == "x":
            finalList = set(lista)
            print(f"Your favorite color/s are: {finalList}")
            x = input("\nEnter any input to continue.")
            break
        else:
            print("Invalid color.")
    return lista

def testing():
    print("Enter your Python code (or type 'exit' to return):")
    user_code = ""
    while True:
        line = input(">>> ")
        if line.lower() == 'exit':
            break
        user_code += line + "\n"
    
    try:
        print("OUTPUT:\n")
        exec(user_code)
        print("\nEnter any input to continue.")
        x = input("")
    except Exception as e:
        print(f"Error: {e}")

def Print():
    while True:
        os.system('cls')
        print("Print Statements Menu")
        print("1. Overview")
        print("2. Examples")
        print("3. Test Code")
        print("4. Return to Menu")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            os.system('cls') 
            print("ＰＲＩＮＴ ＳＴＡＴＥＭＥＮＴＳ\n\nThe print() function in Python is used to output data to the console or terminal.")
            print("It can print strings, variables, or even more complex data types like lists or dictionaries.")
            print("This is a very useful function for debugging, testing, or outputting results to the user.")
            print("\nYou can use the print() function to print various types of data:")
            print("- Strings: print('Hello, World!')")
            print("- Numbers (integers or floats): print(42), print(3.14)")
            print("- Lists, tuples, or dictionaries: print([1, 2, 3]), print({'key': 'value'})")
            print("- Formatted output using f-strings, the str.format() method, or the % formatting.")
            print("\nThe print() function can also handle multiple values separated by commas, printing them with a space in between.")
            print("You can also change the separator between values using the 'sep' argument.")
            print("\nFor better formatting, Python 3.6+ supports f-strings for embedding variables into strings:")
            x = input("\nEnter any input to continue.")
        elif choice == "2":
            os.system('cls')
            print("ＥＸＡＭＰＬＥＳ：")
            print("print('Hello, world!')  # This will print the string 'Hello, world!'")
            print("\nYou can also print variables and expressions:")
            print("name = 'Alice' ")
            print("age = 30")
            print("print(name, age)  # Output: Alice 30")
            print("\nFormatted strings allow embedding expressions inside a string:")
            print("print(f'Name: {name}, Age: {age}')  # Output: Name: Alice, Age: 30")
            print("\nList Example:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("print(fruits)  # Output: ['apple', 'banana', 'cherry']")
            x = input("\nEnter any input to continue.")
        elif choice == "3":
            testing()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def Statements():
    while True:
        os.system('cls')
        print("Statements Menu")
        print("1. Overview")
        print("2. Examples")
        print("3. Test Code")
        print("4. Return to Menu")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            os.system('cls') 
            print("ＳＴＡＴＥＭＥＮＴＳ\n\nA statement in Python is an instruction executed by the Python interpreter. ")
            print("It can be an assignment statement (assigning a value to a variable), a function call, or a control flow statement (like 'if' or 'for').")
            print("\nPython executes statements sequentially, one after the other, unless a control structure like loops or conditionals alter the flow.")
            print("An assignment statement assigns a value to a variable:")
            print("x = 5  # This is an assignment statement.")
            print("\nA function call is a statement that invokes a function:")
            print("print('Hello')  # Function call statement")
            print("\nControl flow statements such as 'if', 'else', and 'for' alter the program’s flow based on conditions or iterations.")
            print("Example of a conditional statement:")
            print("if x > 3:")
            print("    print('x is greater than 3')")
            x = input("\nEnter any input to continue.")
        elif choice == "2":
            os.system('cls')
            print("ＥＸＡＭＰＬＥＳ：")
            print("x = 5  # Assignment statement")
            print("print(x)  # Calling the print function is also a statement")
            print("\nConditional statement example:")
            print("if x > 3:")
            print("   print('x is greater than 3')  # Control flow statement")
            print("\nLoop statement example:")
            print("for i in range(3):")
            print("   print(i)  # Repeats this print statement 3 times")
            x = input("\nEnter any input to continue.")
        elif choice == "3":
            testing()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def Variables():
    while True:
        os.system('cls')
        print("Variables Menu")
        print("1. Overview")
        print("2. Examples")
        print("3. Test Code")
        print("4. Return to Menu")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            os.system('cls') 
            print("ＶＡＲＩＡＢＬＥＳ\n\nVariables are used to store data values. In Python, you don't need to explicitly declare a variable's type; Python will infer it automatically.")
            print("You can assign data to a variable using the assignment operator '='.")
            print("\nFor example:")
            print("x = 5  # x is a variable storing the value 5")
            print("name = 'Alice'  # 'name' is a variable storing a string")
            print("\nVariables can hold different types of data, including:")
            print("- Integers: x = 10")
            print("- Floats: y = 3.14")
            print("- Strings: name = 'Alice'")
            print("- Lists: fruits = ['apple', 'banana']")
            print("\nVariables in Python are mutable, meaning you can reassign a new value to them.")
            x = input("\nEnter any input to continue.")
        elif choice == "2":
            os.system('cls')
            print("ＥＸＡＭＰＬＥＳ：")
            print("x = 10")
            print("y = 20")
            print("z = x + y  # Now z is assigned the sum of x and y")
            print("print(z)  # Output: 30")
            print("\nYou can also store different data types in variables:")
            print("name = 'John'  # String")
            print("isRunning = True  # Boolean")
            print("balance = 300.50  # Float")
            x = input("\nEnter any input to continue.")
        elif choice == "3":
            testing()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def Operators():
    while True:
        os.system('cls')
        print("Operators Menu")
        print("1. Overview")
        print("2. Examples")
        print("3. Test Code")
        print("4. Return to Menu")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            os.system('cls') 
            print("ＯＰＥＲＡＴＯＲＳ\n\nOperators are symbols that perform operations on variables and values. Python supports many types of operators:")
            print("- Arithmetic operators: +, -, *, /, %, **, //")
            print("- Comparison operators: ==, !=, >, <, >=, <=")
            print("- Logical operators: and, or, not")
            print("- Assignment operators: =, +=, -=, *=, /=")
            print("- Bitwise operators: &, |, ^, ~, <<, >>")
            print("- Membership operators: in, not in")
            print("- Identity operators: is, is not")
            print("\nArithmetic operators are used for mathematical operations. For example:")
            print("x = 10 + 5  # Addition")
            print("y = 10 - 5  # Subtraction")
            x = input("\nEnter any input to continue.")
        elif choice == "2":
            os.system('cls')
            print("ＥＸＡＭＰＬＥＳ：")
            print("Arithmetic operators:")
            print("x = 10")
            print("y = 5")
            print("print(x + y)  # Output: 15")
            print("print(x - y)  # Output: 5")
            print("\nComparison operators:")
            print("x = 5")
            print("y = 5")
            print("print(x == y)  # Output: True")
            print("print(x != y)  # Output: False")
            x = input("\nEnter any input to continue.")
        elif choice == "3":
            testing()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def Conditionals():
    while True:
        os.system('cls')
        print("Conditionals Menu")
        print("1. Overview")
        print("2. Examples")
        print("3. Test Code")
        print("4. Return to Menu")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            os.system('cls') 
            print("ＣＯＮＤＩＴＩＯＮＡＬＳ\n\nConditional statements allow you to execute certain blocks of code depending on a condition.")
            print("The most common conditional statements are 'if', 'else', and 'elif'.")
            print("\nThe 'if' statement evaluates a condition and runs the block of code that follows if the condition is True.")
            print("The 'else' statement is used when the condition in the 'if' statement is False.")
            print("The 'elif' (short for 'else if') allows you to check multiple conditions.")
            x = input("\nEnter any input to continue.")
        elif choice == "2":
            os.system('cls')
            print("ＥＸＡＭＰＬＥＳ：")
            print("if age >= 18:")
            print("   print('Adult')")
            print("else:")
            print("   print('Minor')")
            print("\nYou can use 'elif' for multiple conditions:")
            print("if age > 18:")
            print("   print('Adult')")
            print("elif age == 18:")
            print("   print('Just turned 18')")
            print("else:")
            print("   print('Minor')")
            x = input("\nEnter any input to continue.")
        elif choice == "3":
            testing()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def Loops():
    while True:
        os.system('cls')
        print("Loops Menu")
        print("1. Overview")
        print("2. Examples")
        print("3. Test Code")
        print("4. Return to Menu")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            os.system('cls') 
            print("ＬＯＯＰＳ\n\nLoops allow us to iterate over a sequence (like a list or string) or execute a block of code multiple times.")
            print("The two most common loops in Python are 'for' loops and 'while' loops.")
            print("\nA 'for' loop iterates over a sequence of elements, such as a range of numbers or a list.")
            print("A 'while' loop runs as long as a condition is True.")
            print("\nExample of a 'for' loop:")
            print("for i in range(3):")
            print("   print(i)  # Output: 0 1 2")
            x = input("\nEnter any input to continue.")
        elif choice == "2":
            os.system('cls')
            print("ＥＸＡＭＰＬＥＳ：")
            print("for i in range(5):")
            print("   print(i)  # Output: 0 1 2 3 4")
            print("\nWhile loop example:")
            print("i = 0")
            print("while i < 5:")
            print("   print(i)  # Output: 0 1 2 3 4")
            x = input("\nEnter any input to continue.")
        elif choice == "3":
            testing()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")

def Lists():
    while True:
        os.system('cls')
        print("Lists Menu")
        print("1. Overview")
        print("2. Examples")
        print("3. Test Code")
        print("4. Return to Menu")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            os.system('cls') 
            print("ＬＩＳＴＳ\n\nA list is a collection of items in a specific order. Lists are mutable, meaning their contents can be changed.")
            print("You can create a list by enclosing elements in square brackets and separating them by commas.")
            print("\nExample:")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("Lists can contain elements of different data types:")
            print("mixed = [1, 'hello', 3.14, True]")
            x = input("\nEnter any input to continue.")
        elif choice == "2":
            os.system('cls')
            print("ＥＸＡＭＰＬＥＳ：")
            print("fruits = ['apple', 'banana', 'cherry']")
            print("print(fruits[0])  # Output: apple  (Accessing the first element of the list)")
            print("\nYou can add elements to a list:")
            print("fruits.append('orange')  # Adds 'orange' to the end of the list")
            print("\nLists can also be sliced:")
            print("print(fruits[1:3])  # Output: ['banana', 'cherry']  (Accesses the 2nd and 3rd elements)")
            x = input("\nEnter any input to continue.")
        elif choice == "3":
            testing()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please try again.")
            
#Main Code
def Mainmenu():
    global running
    while running:
        os.system('cls')
        print("Ｍａｉｎ   Ｍｅｎｕ - Choose which one you would like to browse. (1-8)")
        print("1. Variables")
        print("2. Statements")
        print("3. Operators")
        print("4. Loops")
        print("5. Lists")
        print("6. Conditionals")
        print("7. Print Statements")
        print("8. Exit Program")
        
        choice = input("Please select an option (1-8): ")
        
        if choice == "1":
            Variables()
        elif choice == "2":
            Statements()
        elif choice == "3":
            Operators()
        elif choice == "4":
            Loops()
        elif choice == "5":
            Lists()
        elif choice == "6":
            Conditionals()
        elif choice == "7":
            Print()
        elif choice == "8":
            running = False
            print("Program closed. Thank you!")
            break
        else:
            os.system('cls')
            print("Invalid choice. Please try again.")
            x = input("Enter any input to continue.")

First()
Mainmenu()
