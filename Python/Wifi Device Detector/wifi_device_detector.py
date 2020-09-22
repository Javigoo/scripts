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

def warning_unsafe_page(driver):
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

    login()
    username.send_keys(getUsername())
    password.send_keys(getPassword())
    password.send_keys(Keys.RETURN)

def get_wifi_devices(driver):
    devices = []

    try:
        # Wait as long as required, or maximum of 10 sec for alert to appear
        wait = WebDriverWait(driver, 10)
        connected_devices = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div/div[1]')))

    except:
        print('TIMEOUT - get_wifi_devices')

    sleep(1)
    source_code = connected_devices.get_attribute("outerHTML")
    connected_devices = source_code.split('<div class="text small-text">')

    for device in connected_devices[1:]:
        device_name = device.split()[0]
        devices.append(device_name)

    return devices

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

if __name__ == "__main__":

    driver = open_webdriver()
    login_router(driver)
    devices = get_wifi_devices(driver)

    print('Dispositivos conectados:', ', '.join(devices) + '\n')

    with open('device-proprietary.dat', 'r') as device_proprietary_list:
        for device_proprietary in device_proprietary_list:
            device = device_proprietary.split()[0]
            proprietary = device_proprietary.split()[1]

            if device in devices:
                print(proprietary + ' está conectado con ' + device)