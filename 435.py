#435

hőalsó = float(input("Eszköz alsó hőmérséklet határa:"))
hőfelső = float(input("Eszköz felső hőmérséklet határa:"))

if hőalsó < 25 and hőfelső > 85:
	print("Az eszköz katonai célokra megfelel.")
