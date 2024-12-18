#See if you have passed the course
#Below you will need to input your grades

prelims = eval(input("Enter prelims average."))
midterm = eval(input("Enter midterm average."))
semifinals = eval(input("Enter semifinals average."))
finals = eval(input("Enter finals average."))
quiz =  eval(input("Enter quiz average."))
project = eval(input("Enter project average."))

#Grades section

resu = (prelims * 0.15) + (midterm * 0.15) + (semifinals + 0.15) + (finals * 0.15) + (quiz * 0.15) + (project * 0.15)
result = round(resu, 2)

if result >= 75 :
	print(f"The result is" ,result, "therefore you passed the course, congratulations!")

else :
	print("Sorry, you did not pass. Do better next time!")




