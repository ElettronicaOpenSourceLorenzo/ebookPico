import machine
import utime

spi_sck=machine.Pin(2)
spi_tx=machine.Pin(3)
spi_rx=machine.Pin(4)

spi=machine.SPI(0,baudrate=100000,sck=spi_sck,mosi=spi_tx,miso=spi_rx)


adc = machine.ADC(4)


fattore_conversione = 3.3 / (65535)

while True:
    lettura = adc.read_u16() * fattore_conversione
    
    temperatura_celsius = 25 - (lettura - 0.706)/0.001721
    
    spi.write('\x7C')
    spi.write('\x2D')
    
    
stringa_da_stampare = "Temp: " + str(temperatura_celsius)
    
    spi.write(stringa_da_stampare)
    
    
utime.sleep(2)