#427

testsuly = float(input("Testsúly(kg):"))
magassag = float(input("Magasság(m):"))
tmi = testsuly / magassag**2

print("Testtömegindex:", tmi)

if tmi < 16:
	print("Súlyos soványság.")
if tmi > 16 and tmi < 16.99:
	print("Mérsékelt soványság.")
if tmi > 17 and tmi < 18.49:
	print("Enyhe soványság.")
if tmi > 18.5 and tmi <24.99:
	print("Normális testsúly.")
if tmi >25 and tmi < 29.99:
	print("Túlsúlyos.")
if tmi > 30 and tmi < 34.99:
	print("I. fokú elhízás.")
if tmi > 35 and tmi < 39.99:
	print("II. fokú elhízás.")
if tmi >=40:
	print("III. fokú (súlyos) elhízás.")
