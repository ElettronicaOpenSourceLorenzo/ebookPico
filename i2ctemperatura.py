import machine
import utime


sda=machine.Pin(0)

scl=machine.Pin(1)


i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)


adc = machine.ADC(4)


fattore_conversione = 3.3 / (65535)

while True:
    lettura = adc.read_u16() * fattore_conversione
    
    temperatura_celsius = 25 - (lettura - 0.706)/0.001721
    
    i2c.writeto(114, '\x7C')
    i2c.writeto(114, '\x2D')
    
    
stringa_da_stampare = "Temp: " + str(temperatura_celsius)
    
    i2c.writeto(114, stringa_da_stampare)
    
    
utime.sleep(2)