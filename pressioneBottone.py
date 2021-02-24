""" Lorenzo Neri - Elettronica Open Source
"""

# importo i pacchetti necessari
import machine
import utime
import _thread

# imposto la variabile per leggere la pressione del bottone
bottone = Pin(12, Pin.In, Pin.PULL_DOWN)

# creo una variabile globale per il thread
global bottone_premuto

# la imposto inizialmente a False (non è premuto)
bottone_premuto = False

# creo la funzione da eseguire nel thread
def funzione_bottone_thread():
    
    global bottone_premuto
    
    while True:
        # se il valore letto dalla GPIO è "1" vuol dire che il bottone è stato premuto
        if bottone.value() == 1:
            bottone_premuto = True


# faccio partire il thread
_thread.start_new_thread(funzione_bottone_thread, ())

# eseguo il ciclo principale del programma
while True:
    # comunico a video quando il bottone è stato premuto
    if bottone_premuto == True:
        print("Il bottone è stato premuto")
        
        """ imposto a False forzatamente. Questo è necessario 
            perché diversamente vedremo un'infinità di messaggi a console
            fintanto che l'utente tiene premuto il bottone
        """
        global bottone_premuto
        bottone_premuto = False
