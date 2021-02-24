# librerie necessarie
import machine
import utime

# usiamo il canale numero 4 dell'ADC di Pico per rilevare
sensor_temp = machine.ADC(4)
# fattore di conversione necessario 
conversion_factor = 3.3 / (65535)



# cicliamo all'infinito
while True:

    # leggiamo la temperatura
    lettura = sensor_temp.read_u16() * conversion_factor

    # correggiamo assieme al fattore di conversione per trasformare in Celsius
    temperatura = 27 - (lettura - 0.706)/0.001721
    # stampiamo a video
    print(temperatura)

    # apriamo il nostro file in modalità "append"
    file_dati = open("temp.txt","a")

    # scriviamo nel file
    file_dati.write(str(temperatura)+" - ")

    # chiudiamo il file in modalità "flush"
    file_dati.flush()

    # attendiamo due secondi
    utime.sleep(2)