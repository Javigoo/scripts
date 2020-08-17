#!/bin/env python3

import sys
import requests
  
# api-endpoint 
URL = "https://vrmapi.victronenergy.com/v2/"

def login():

    # Parameters to be sent to the API 
    url_login = URL + "auth/login"
    data_login = '{"username": "john@example.com","password": "secret-passw0rd"}'
    
    # sending request and saving the response as response object 
    r = requests.post(url = url_login, data=data_login) 
    data = r.json()

    if len(data) > 2:
        sys.stderr.write('ERROR: '+data['errors']+'\n')
        exit(-1)
        
    # extracting data in json format 
    return data

def getToken(data):

    return data['token']

def getIdUser(data):

    return data['idUser']

def get_installation_info(idUser, token):

    # Parameters to be sent to the API
    url_info = URL + "users/"+str(idUser)+"/installations"
    params_info = {'extended':1}
    headers_info = {'X-Authorization': "Bearer "+ str(token)}

    # sending request and saving the response as response object
    r = requests.get(url = url_info, params=params_info, headers=headers_info) 
    
    # extracting data in json format 
    return r.json() 

def get_solar_yield(data):

    return data['records'][0]['extended'][12]['formattedValue']
  
if __name__ == "__main__":

    data_login = login()
    data_installation = get_installation_info(getIdUser(data_login), getToken(data_login))
    produccion_solar = get_solar_yield(data_installation)

    if produccion_solar == "0 W":
        print("Es de noche")
    else:
        print("Es de día")
        print("La producción solar es de", produccion_solar)
