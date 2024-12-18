name = input ("What is your name?")
age = input ("What is your age?")
email = input ("Please enter your email.")

print ("Welcome, " + name + ". Our systems have received the information regarding your age and email. \n " + name + ", " + age + " years old. \n Email: " + email + ".")

num1 = eval(input("Give me a number."))
num2 = eval(input("Another one."))

ans1 = num1 + num2
ans2 = num1 - num2
ans3 = num1 * num2
ans4 = num1 / num2
ans5 = num1 % num2
ans6 = num1 ** num2
ans7 = num1 // num2

print ("The sum of" , num1 , "and" , num2 , "is" , ans1 , ".")
print ("The difference of" , num1 , "and" , num2 , "is" , ans2 , ".")
print ("The product of" , num1 , "and" , num2 , "is" , ans3 , ".")
print ("The quotient of" , num1 , "and" , num2 , "is" , ans4 , "." )
print ("The exponent by" , num2 , "is" , ans5 ,)
print ("The remainder of" , num1 , "and" , num2 , "is" , ans6 ,)
print ("The floor division of" , num1 , "and" , num2 , "is" , ans7 ,)