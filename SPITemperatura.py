""" Lorenzo Neri - Elettronica Open Source
"""

# importo i pacchetti necessari
import machine
import utime

# imposto i collegamenti con SCK, TX ed RX
spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi_rx=machine.Pin(4)

# imposto la comunicazione SPI
spi=machine.SPI(0,baudrate=100000,sck=spi_sck,mosi=spi_tx,miso=spi_rx)

# imposto la variabile per la rilevazione di temperatura dal sensore built-in
adc = machine.ADC(4)

# imposto il fattore di conversione
fattore_conversione = 3.3 / (65535)

while True:

    # eseguo la lettura della temperatura
    lettura = adc.read_u16() * fattore_conversione
    
    # la converto in gradi Celsius
    temperatura_celsius = 27 - (lettura - 0.706)/0.001721
    
    # invio i comandi SPI (in questo caso non serve specificare l'indirizzo)
    spi.write('\x7C')
    spi.write('\x2D')
    
    
    # racchiudo tutto in una stringa
    stringa_da_stampare = "Temperatura: " + str(temperatura_celsius)
    
    # stampo la stringa nel display
    spi.write(stringa_da_stampare)
    
    # attendo due secondi
    utime.sleep(2)