from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

import json
import os
import time

import module.helpers as h

SEGUNDOS_ENTRE_FATURAS = 3

def run(faturas, user):

    # get current directory
    path = os.getcwd()
    # go to parent folder 
    path = os.path.abspath(os.path.join(path, os.pardir))

    # print(path)

    # print(f"{path}\\config\\users.json")

    # load json file
    f = open(path + "\\config\\users.json")
    data = json.load(f)
    try:
        user = data['users'][user]
    except IOError as error:
        print(error)
        exit

    username = user['name']
    password = user['password']


    with Firefox(executable_path = path + '\core\Selenium\geckodriver.exe') as driver:
        # Login
        driver.get("https://www.acesso.gov.pt/jsp/loginRedirectForm.jsp?path=registarDocumentoEmitenteForm.action&partID=EFPF")
        username_box = driver.find_element_by_name("username")
        username_box.send_keys(username)
        password_box = driver.find_element_by_name("password")
        password_box.send_keys(password)
        login_btn = driver.find_element_by_name("sbmtLogin")
        login_btn.click()

        for fatura in faturas:

            # Validate if fatura has empty attributes
            if (h.hasEmptyAttribute(fatura)):
                # skip registry
                continue

            try:                   
                # Find «Confirm» button
                driver.get("https://faturas.portaldasfinancas.gov.pt/registarDocumentoEmitenteForm.action")
                nif_box = driver.find_element_by_name("nifAdquirente")
                nif_box.send_keys(fatura.nif)
                # nif_box.send_keys("123456789")
                number_box = driver.find_element_by_name("numeroDocumento")
                number_box.send_keys(fatura.number)
                # number_box.send_keys("1234")
                doctype_box = driver.find_element_by_name("tipoDocumento")
                doctype_box.send_keys("F")
                date_box = driver.find_element_by_name("dataEmissaoDocumento")
                date_box.send_keys(fatura.date)
                # date_box.send_keys("2022-01-12")
                value_box = driver.find_element(By.ID,"total_0")
                value_box.send_keys(fatura.value)
                # value_box.send_keys("5")
                iva_box = driver.find_element(By.ID,"tIva_0")
                iva_box.send_keys("i")
                reason_box = driver.find_element(By.ID,"motivo_0")
                reason_box.send_keys("ii")

                save_btn = driver.find_element(By.ID,"guardarDocumentoBtn")
                save_btn.click()

                error_box = driver.find_element_by_class_name("alert-error")
                if error_box != None:
                    print("Erro ao introduzir a fatura " + fatura.number)

                time.sleep(SEGUNDOS_ENTRE_FATURAS)

            except IOError as error:
                print(error)
                exit
        
        print("End")