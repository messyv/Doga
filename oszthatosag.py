#415

num1 = int(input("Szám="))

if (num1 % 2 == 0) and  (num1 % 3 == 0):
	print("Osztható 2-vel és 3-mal is.")
	
elif num1 % 2 == 0:
	print("A szám osztható kettővel.")
	
elif num1 % 3 == 0:
	print("A szám osztható hárommal.")

else:
	print("A szám se 3-mal, se 2-vel nem osztható.")
