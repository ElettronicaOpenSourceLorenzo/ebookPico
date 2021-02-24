""" Lorenzo Neri - Elettronica Open Source
"""

# importo le librerie
from machine import Pin
import utime

# imposto la variabile per il LED built-in
ledBuiltIn = Pin(25, Pin.OUT)

# imposto il ciclo di accensione/spegnimento per 100 volte
for _ in range(0,100):
    print("accendo il LED")
    ledBuiltIn.value(1)
    
    # aspetto 2 secondi
    utime.sleep(2)
    
    print("spengo il LED")
    ledBuiltIn.value(0)
    
    # aspetto 2 secondi
    utime.sleep(2)
    
    