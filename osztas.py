#410

num1 = float(input("Első szám:"))
num2 = float(input("Második szám:"))

if num1 > num2:
	osztas1 = num1/num2
	print(num1, "osztva",num2, "egyenlő", osztas1,".")
	
elif num1 < num2:
	osztas2 = num2/num1
	print(num2, "osztva",num1, "egyenlő", osztas2,".")
