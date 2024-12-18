#Denominators demonstration
name = input("Please enter your username.")
amount = eval(input("Please enter an amount."))
tsun = amount // 1000
tsun2 = amount % 1000
fhun = tsun2 // 500
fhun2 = tsun2 % 500
thun = fhun2 // 200
thun2 = fhun2 % 200
ohun = thun2 // 100
ohun2 = thun2 % 100
fifty = ohun2 // 50
fifty2 = ohun2 % 50
bente = fifty2 // 20
bente2 = fifty2 % 20
ten = bente2 // 10
ten2 = bente2 % 10
payb = ten2 // 5
payb2 = ten2 % 5
wan = payb2 // 1
wan2 = payb2 % 1

print(tsun, "1000")
print(fhun, "500")
print(thun, "200")
print(ohun, "100")
print(fifty, "50")
print(bente, "20")
print(ten, "10")
print(payb, "5")
print(wan, "1")
