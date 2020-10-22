magasság = 73
oldal_1 = 21
oldal_2 = 47


Terület=2*(oldal_1*oldal_2)
Felszín = 2*(oldal_1*oldal_2+oldal_1*magasság+oldal_2*magasság)
Szigfel = Felszín - Terület

print ("Szigetelendő felszín: ", Szigfel, "m\u00b2")
