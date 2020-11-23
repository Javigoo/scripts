#!/bin/env python3

import os
import sys
import getpass
import requests
  
# api-endpoint 
URL = "https://vrmapi.victronenergy.com/v2/"

def login():
    if 'login.dat' not in os.listdir("."):
        username = str(input("Username: "))
        password = str(getpass.getpass())
        with open('login.dat', 'w') as f: 
            f.write(username)
            f.write(" ")
            f.write(password) 

def getUsername():
    with open('login.dat', 'r') as f:
        return f.readline().split()[0]

def getPassword():
    with open('login.dat', 'r') as f:
        return f.readline().split()[1]

def getLoginInfo():
    # Parameters to be sent to the API 
    url_login = URL + "auth/login"
    data_login = '{"username": "'+getUsername()+'","password": "'+getPassword()+'"}'
    
    # Sending request and saving the response as response object 
    r = requests.post(url = url_login, data=data_login) 

    data = r.json()
    if len(data) > 2:
        sys.stderr.write('ERROR: '+data['errors']+'\n')
        if data['errors'] == "Invalid credentials":
            os.remove("login.dat")
        exit(-1)
        
    return data

def getToken(data):
    return data['token']

def getIdUser(data):
    return data['idUser']

def getInstallationInfo(idUser, token):
    # Parameters to be sent to the API
    url_info = URL + "users/"+str(idUser)+"/installations"
    params_info = {'extended':1}
    headers_info = {'X-Authorization': "Bearer "+ str(token)}

    # Sending request and saving the response as response object
    r = requests.get(url = url_info, params=params_info, headers=headers_info) 
    
    return r.json() 

def getSolarYield(data):
    return data['records'][0]['extended'][12]['formattedValue']
  
if __name__ == "__main__":
    login()
    data_login = getLoginInfo()
    data_installation = getInstallationInfo(getIdUser(data_login), getToken(data_login))
    produccion_solar = getSolarYield(data_installation)

    if produccion_solar == "0 W":
        print("Es de noche")
    else:
        print("Es de día")
        print("La producción solar es de", produccion_solar)
