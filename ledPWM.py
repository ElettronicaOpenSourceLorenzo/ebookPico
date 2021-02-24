""" Lorenzo Neri - Elettronica Open Source
"""

# importo i pacchetti necessari
import time
from machine import Pin, PWM

# imposto il LED built-in come PWM
ledPWM = machine.PWM(machine.Pin(25))

# imposto la frequenza del segnale
ledPWM.freq(1000)

# ciclo
while True:
    print("Accendo un passo per volta il LED")

    # eseguo il ciclo per accendere gradualmente il LED
    for luminosita in range(0,65535, 1024):
        print(luminosita)
        ledPWM.duty_u16(luminosita)
        utime.sleep(0.2)
        
    # imposto il valore massimo e aspetto 2 secondi
    ledPWM.duty_u16(65535)
    
    utime.sleep(2)
    
    print("Spegno un passo per volta il LED")    
    # eseguo il ciclo per spegnere gradualmente il LED
    for luminosita in range(65535, 0, -1024):
        print(luminosita)
        ledPWM.duty_u16(luminosita)
        utime.sleep(0.2)
    # spegno totalmente il LED
    ledPWM.duty_u16(0)
    utime.sleep(2)
