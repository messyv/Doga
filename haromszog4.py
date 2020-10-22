#406
print("Szitás-Kiss Vanda")
print("Ez a program megnézi, hogy szerkeszthető- e egy háromszög \na megadott oldalai alapján és ha igen, akkor kiírja a kerületét.")

a = int(input("Háromszög első oldala:"))
b = int(input("Háromszög második oldala:"))
c = int(input("Háromszög harmadik oldala:"))

if a+b > c and b+c >a and a+c > b:
	kerület = a + b + c
	print("A háromszög kerülete:", kerület)
	
else:
	print("A háromszög nem szerkeszthető.")
