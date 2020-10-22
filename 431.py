#431

nev = input("Név:")
alapber = float(input("Alapbér:"))
jutt = float(input("Juttatások:"))
nyelv = float(input("Nyelvi pótlék:"))

jovedelem = alapber + jutt + nyelv

if jovedelem > 1000000:
	ado1 = (jovedelem*36)/100
	print(nev, "fizetendő adója:", ado1)
	
if jovedelem < 1000000:
	ado2 = (jovedelem*16)/100
	print(nev, "fizetendő adója:", ado2, "Ft")
