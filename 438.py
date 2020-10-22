#438

kredit = float(input("Elért kreditpontok:"))
jegyatlag = float(input("Osztályzatok átlaga:"))
osztondijindex = kredit*jegyatlag / 30

print ("Ösztöndíj átlag:", osztondijindex)

if osztondijindex > 5.8:
	print ("Jó eredmény.")
else:
	print("Gyenge eredmmény.")
	
	
