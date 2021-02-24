""" Lorenzo Neri - Elettronica Open Source
"""

# importo i pacchetti necessari
import machine
import utime

# imposto il pin a cui è collegato il potenziometro
potenziometro = machine.ADC(26)

# imposto il fattore conversione per l'ADC
fattore_conversione = 3.3 / 65535

while True:

    # moltiplico il valore letto per il fattore di conversione
    # in questo modo ottengo un valore fra 0 e 3,3V.
    tensione_letta = potenziometro.read_u16() * fattore_conversione
    print("Valore letto:")
    print(tensione_letta)
    
    # aspetto due secondi
    utime.sleep(2)