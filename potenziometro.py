""" Lorenzo Neri - Elettronica Open Source
"""

import machine
import utime

potenziometro = machine.ADC(26)


while True:
    print("Valore letto:")
    print(potenziometro.read_u16())
    utime.sleep(2)