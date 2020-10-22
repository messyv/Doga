#422

flour = float(input("Liszt mennyiség(kg):"))
honey = float(input("Méz mennyiség(kg):"))
milk = float(input("Tej mennyiség(l):"))

vegosszeg = (flour* 300) + (honey * 1000) + (milk * 200)

print ("Végösszeg:", vegosszeg, "Ft")

if vegosszeg > 10000:
	print("Nem elegendő pénz.")
