# Cita-previa-renovacion-asilo-Alicante
  Script escrito en Python que usa Selenium para automatizar el proceso de pedir cita para la renovación de asilo en Alicante.

  Para usarlo, abrir el archivo Cita.py y en la línea 12 modificar los valores "TuNie" "TuNombre" 1111 "TuPais" por tus respectivos datos, es importante 
  escribir los valores entre comillas menos la fecha de nacimiento.

  Para ejecutar, abres la terminal, vas a la dirección donde lo tengas descargado y lo ejecutas con: python Cita.py

                                                                  **NUEVO**
  
  Para evitar el bloqueo temporal al realizar muchas peticiones a la web de extranjería puedes añadir el siguiente fragmento de codigo al programa para que cada x 
  iteraciones vayas cambiando de IP. Para ello uso NordVPN (de pago).

  Añadir un contador en el codigo que se llame vpn y que vaya aumentando por cada iteración, en este caso la ip cambiará cada 10 iteraciones.
  ```
        if vpn % 10 == 0:
            try:
                subprocess.run(['nordvpn', '-c'], check=True)
            except:
                pass
            time.sleep(8)
```
  
