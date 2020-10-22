#419

osztando = int(input("Osztandó:"))
oszto = int(input("Osztó:"))
hanyados = osztando / oszto
maradek = osztando % oszto

print("A hányados:", hanyados)
print("A maradék:", maradek)

if maradek == 0:
	print ("Nem volt maradék.")
else:
	print ("Volt maradék.")
