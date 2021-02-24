import machine
import utime
import _thread

bottone = Pin(12, Pin.In, Pin.PULL_DOWN)

global bottone_premuto

bottone_premuto = False

def funzione_bottone_thread():
    
    global bottone_premuto
    
    while True:
        if bottone.value() == 1:
            bottone_premuto = True


_thread.start_new_thread(funzione_bottone_thread, ())

while True:
    if bottone_premuto == True:
        print("Il bottone è stato premuto")
        
        global bottone_premuto
        bottone_premuto = False
