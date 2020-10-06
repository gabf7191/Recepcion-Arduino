# Recepcion.Arduino
 Recepcion de envios contra base de datos y comunicacion con Arduino (Relay Out) 


El usuario lee un envio mediante un codigo de barra.
El programa lo compara contra una base (Google Sheets, para las pruebas preliminares), y si el envio existe, abre el puerto serial para comunicarse con el arduino. 
El arduino recibe esta informacion y actua segun lo programado. (En el Arduino se puenteo el reset (Resistencia 1Kohm) y se conectaron 2 salidas digitales a una placa de relay (Luego a 2 motores))

*Aclaracion* En este repositorio se borraron las credenciales para acceder a la base, por una cuestion de seguridad. 

