""" Lorenzo Neri - Elettronica Open Source
"""

# importo i pacchetti necessari
import machine
import utime

# imposto il pin a cui è collegato il potenziometro
potenziometro = machine.ADC(26)


while True:
    print("Valore letto:")
    # eseguo una lettura ogni due secondo del potenziometro
    print(potenziometro.read_u16())
    utime.sleep(2)