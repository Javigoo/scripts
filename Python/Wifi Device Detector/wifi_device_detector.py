#!/bin/env python3

import os
import sys
import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_webdriver():
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    DRIVER_PATH = os.getcwd()+'/chromedriver'

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get('http://192.168.0.1/overview.html')

    return driver

def skip_warning_unsafe_page(driver):
    driver.find_element_by_id('details-button').click()
    driver.find_element_by_id('proceed-link').click()
    
def login_router(driver):
    try:
        # Wait as long as required, or maximum of 5 sec for alert to appear
        wait = WebDriverWait(driver, 5)
        username = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="activation-content-right"]/div[2]/div/input')))
        password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="activation-content-right"]/div[3]/div[1]/input')))

    except:
        print('TIMEOUT - login_router')
        sys.exit(-1)

    get_login_data()
    username.send_keys(get_username())
    password.send_keys(get_password())
    password.send_keys(Keys.RETURN)

def get_wifi_devices(driver):
    devices = []

    try:
        # Wait as long as required, or maximum of 10 sec for alert to appear
        wait = WebDriverWait(driver, 15)
        connected_devices = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div/div[1]')))

    except:
        print('TIMEOUT - get_wifi_devices')
        sys.exit(-1)

    source_code = connected_devices.get_attribute("outerHTML")
    connected_devices = source_code.split('<div class="text small-text">')

    for device in connected_devices[1:]:
        device_name = device.split()[0]
        devices.append(device_name)

    return devices

def get_login_data():
    if 'login.dat' not in os.listdir("."):
        username = str(input("Username: "))
        password = str(getpass.getpass())
        with open('login.dat', 'w') as f: 
            f.write(username)
            f.write(" ")
            f.write(password) 

def get_username():
    with open('login.dat', 'r') as f:
        return f.readline().split()[0]

def get_password():
    with open('login.dat', 'r') as f:
        return f.readline().split()[1]

def device_proprietary_parser():
    proprietary_devices_list = {}

    with open('device-proprietary.dat', 'r') as device_proprietary_data:
        for device_proprietary in device_proprietary_data:
            proprietary = device_proprietary.split(':')[0]
            device = device_proprietary.strip().split(':')[1].split(',')
            proprietary_devices_list[proprietary] = device
    
    return proprietary_devices_list

def get_proprietary_connected_devices(connected_devices, proprietary_devices_list):
    proprietary_connected_devices_list = {}

    # Listar todos los dispositivos conectados de un propietario
    for proprietary in proprietary_devices_list.keys():
        proprietary_connected_devices = []
        for device in connected_devices:
            if device in proprietary_devices_list[proprietary]:
                proprietary_connected_devices.append(device)

        proprietary_connected_devices_list[proprietary] = proprietary_connected_devices

    return proprietary_connected_devices_list

def show_proprietary_connected_devices(proprietary_connected_devices):
    for proprietary in proprietary_connected_devices.keys():
        print(proprietary+' conectado con '+ ', '.join(proprietary_connected_devices[proprietary]))

def show_unknown_connected_devices(connected_devices, known_connected_devices):
    unknown_connected_devices = []
    known_connected_devices = [item for sublist in known_connected_devices for item in sublist]

    for device in connected_devices:
        if device not in known_connected_devices:
            unknown_connected_devices.append(device)

    print('\nDispositivos desconocidos: '+', '.join(unknown_connected_devices))

if __name__ == "__main__":
    driver = open_webdriver()
    login_router(driver)
    connected_devices = get_wifi_devices(driver)

    print('Dispositivos conectados:', ', '.join(connected_devices) + '\n')

    device_proprietary_list = device_proprietary_parser()

    proprietary_connected_devices = get_proprietary_connected_devices(connected_devices, device_proprietary_list)

    show_proprietary_connected_devices(proprietary_connected_devices)
    show_unknown_connected_devices(connected_devices, proprietary_connected_devices.values())