""" Lorenzo Neri - Elettronica Open Source
"""

import machine
import utime

potenziometro = machine.ADC(26)

fattore_conversione = 3.3 / 65535

while True:
    tensione_letta = potenziometro.read_u16() * fattore_conversione
    print("Valore letto:")
    print(tensione_letta)
    utime.sleep(2)