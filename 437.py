#437

szélseb = float(input("Szélsebesség(km/h):"))
kifut1 = float(input("Szélirány 1-es kifutóhoz képest:"))
felhő = float(input("Felhősödés arányszáma:"))



if szélseb > 50 and kifut1 > 30:
	print("Nem ajánlott a felszállás.")
elif szélseb < 0 or szélseb > 500 or kifut1 < 0 or kifut1 >180:
	print("Error. Szélsebesség vagy szélirány intervallumon kívül!")
if szélseb > 100:
	print("Tiltott felszállás.")
elif szélseb < 0 or szélseb > 500:
	print("Error. Szélsebesség intervallumon kívül!")
if felhő > 45:
	print("Tiltott felszállás.")
elif felhő < 1 or felhő > 100:
	print("Error. Felhősödés intervallumon kívül!")
