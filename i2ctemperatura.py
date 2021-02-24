""" Lorenzo Neri - Elettronica Open Source
"""


# importo i pacchetti necessari
import machine
import utime

# imposto i pin a cui abbiamo connesso SDA ed SCL del display
sda = machine.Pin(0)
scl = machine.Pin(1)

# imposto la comunicazione I2C
i2c = machine.I2C(0,sda=sda, scl=scl, freq=400000)

# imposto la variabile per la rilevazione di temperatura dal sensore built-in
adc = machine.ADC(4)

# imposto il fattore di conversione
fattore_conversione = 3.3 / (65535)

while True:

    # eseguo la lettura della temperatura
    lettura = adc.read_u16() * fattore_conversione
    
    # la converto in gradi Celsius
    temperatura_celsius = 27 - (lettura - 0.706)/0.001721
    
    # invio i comandi I2C
    i2c.writeto(114, '\x7C')
    i2c.writeto(114, '\x2D')
    
    # racchiudo tutto in una stringa
    stringa_da_stampare = "Temperatura: " + str(temperatura_celsius)
    
    # stampo sul display
    i2c.writeto(114, stringa_da_stampare)
    
    # attendo due secondi
    utime.sleep(2)