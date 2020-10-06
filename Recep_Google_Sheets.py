#Programa de recepcion contra la base de Google sheets

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import serial, time
import ArduinoConnect

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("Creds.json", scope)

client = gspread.authorize(creds)

sheetEnv = client.open("Envios").sheet1 #Abro el archivo de envios y el de recepcion
sheetRec = client.open("Recepcion").sheet1

dataEnv = sheetEnv.get_all_records() #Recupero la info entera de las DB
dataRec = sheetRec.get_all_records()

Envio = input("Inserte numero de envio")  #Scaneo Paquete

t = time.localtime() #Guardo la hora del scaneo
current_time = time.strftime("%H:%M:%S", t)


List_Envios = sheetEnv.col_values(1)      #Agarro la columna de envios

Aceptado = "No Ok" #Boolean

for line in List_Envios:   #Busco mi paquete, y actualizo la boolean

    if line == Envio:
        Aceptado = "ok"



if Aceptado == "ok":
    datos = [Envio, current_time ] #Linea a escribir
    Ult = len(dataRec) + 2
    sheetRec.insert_row(datos, Ult)
    ArduinoConnect.Arranque()


print ("Envio " + str(Envio) + " esta " + str(Aceptado))


