#Here in this instance, I require you to input your name, address, and age.
#This will determine what age group you are in

name = input("What is your name?")
address = input("Where do you reside in?")
age = eval(input("Drake asks for your age, answer him through this instance."))

if age >= 1 and age <= 8 :
	print(f"Hi {name} from {address}, age {age}. Toddler stage.")
elif age >= 9 and age <= 14 :
	print(f"Hi {name} from {address}, age {age}. Preteen stage.")
elif age >= 15 and age <= 18 :
	print(f"Hi {name} from {address}, age {age}. Teenage stage.")
elif age >= 19 and age <= 27 :
	print(f"Hi {name} from {address}, age {age}. Early adulthood stage.")
elif age >= 28 and age <= 44 :
	print(f"Hi {name} from {address}, age {age}. Middle age stage.")
elif age >= 45 and age <= 59 :
	print(f"Hi {name} from {address}, age {age}. Past adulthood stage.")
elif age >= 60 :
	print(f"Hi {name} from {address}, age {age}. Senior stage.")
else :
	print("Just, what are you?")