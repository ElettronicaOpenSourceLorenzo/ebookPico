""" Lorenzo Neri - Elettronica Open Source
"""

# importo i pacchetti necessari
import machine

# imposto i pin a cui abbiamo connesso SDA ed SCL del display
sda = machine.Pin(0)
scl = machine.Pin(1)

# imposto la comunicazione I2C
i2c = machine.I2C(0,sda=sda, scl=scl, freq=400000)

# invio i comandi rispettivamente per "scrivere"
# e impostare il cursorse a inizio display
i2c.writeto(114, '\x7C')
i2c.writeto(114, '\x2D')

# scrivo sul display
i2c.writeto(114, "Ciao sono Pico!")