from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import json
import os
import time

def run():

    # get current directory
    path = os.getcwd()

    # load json file
    f = open(path + "\confs.json")
    data = json.load(f)
    user = data['users'][0]

    # print(user['name'])
    # print(user['password'])
    username = user['name']
    password = user['password']

    with Firefox(executable_path = path + '\Selenium\geckodriver.exe') as driver:
        # Login
        driver.get("https://www.acesso.gov.pt/jsp/loginRedirectForm.jsp?path=registarDocumentoEmitenteForm.action&partID=EFPF")
        username_box = driver.find_element_by_name("username")
        username_box.send_keys(username)
        password_box = driver.find_element_by_name("password")
        password_box.send_keys(password)
        login_btn = driver.find_element_by_name("sbmtLogin")
        login_btn.click()

        # Find «Confirm» button
        driver.get("https://faturas.portaldasfinancas.gov.pt/registarDocumentoEmitenteForm.action")
        nif_box = driver.find_element_by_name("nifAdquirente")
        nif_box.send_keys("123456789")
        number_box = driver.find_element_by_name("numeroDocumento")
        number_box.send_keys("1234")
        doctype_box = driver.find_element_by_name("tipoDocumento")
        doctype_box.send_keys("F")
        date_box = driver.find_element_by_name("dataEmissaoDocumento")
        date_box.send_keys("2022-01-12")
        value_box = driver.find_element(By.ID,"total_0")
        value_box.send_keys("5")
        iva_box = driver.find_element(By.ID,"tIva_0")
        iva_box.send_keys("i")
        reason_box = driver.find_element(By.ID,"motivo_0")
        reason_box.send_keys("ii")
        
        # save_btn = reason_box = driver.find_element(By.ID,"guardarDocumentoBtn")
        # save_btn.click()

        # for btn in confirm_btn:
            # Confirm
            # btn.click()
        
        print("End")