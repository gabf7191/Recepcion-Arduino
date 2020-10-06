import requests as rq
import json
import csv
import pandas as pd

def jprint(obj):
    # cREA UN STRING DEL jSON
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


headers = {
    "Authorization": "Basic cmVjYXRwX3dzOk5uRm85UGhHUnQxUDU="
}

response = rq.get("https://api.andreani.com/login", headers= headers)

print(response.status_code)
Token = response.headers['X-Authorization-token']
print(Token)


headers = {
    "X-Authorization-token": Token
}


#Metodos

#Envio = str(310000011225853)
#Envio pendiente =310000011235853

Envio = str(310000011225853)



Trazas = "https://api.andreani.com/v1/envios/" + Envio + "/trazas"
Orden = "https://api.andreani.com/v2/ordenes-de-envio/" + Envio

response= rq.get(Trazas, headers= headers)

#jprint(response.json())
print(response.json()["eventos"] )

db = pd.read_csv("hola.csv", encoding='latin-1', names = ["Id" , "Ref",  "Loc"])


#FechaDeIngreso = "0"
#FechaDeSalida = "0"
#Suc = "0"

Sucursal = "En espera"

for data in response.json()["eventos"]:
    #Fecha = data["Fecha"]
    #SucActual = data["SucursalId"]
    #if SucActual != data["SucursalId"]:
    #    FechaDeIngreso = Fecha

    print(data["Fecha"])
    for i in range(len(db)):   #Busco en la lista de sucursales, para hacer print del nombre y no del ID
        if db.iloc[i][0] == data["SucursalId"]:
            Sucursal = db.iloc[i][2]

    print (Sucursal)




