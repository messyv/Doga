#274

hossz = 170
szélesség = 17
magasság = 3
másikoldal = szélesség/2

import math
tetőrövidebboldala = float(math.sqrt((magasság**2)*(másikoldal**2)))

tetőterület = 2*(tetőrövidebboldala*hossz)
print (tetőterület, "m\u00b2 cserépre van szükség.")
