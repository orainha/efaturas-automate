from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import json
import os
import time

import module.helpers as h


SECONDS_BETWEEN_FATURAS = 3

def run(faturas, user):
    """ The last stop of this project.
        Having the username and Faturas, we can now insert Faturas into e-faturas using Selenium """

    # Get current directory
    path = os.getcwd()
    # Go to parent folder 
    path = os.path.abspath(os.path.join(path, os.pardir))

    # Load user json file - containing the credentials
    f = open(path + "\\config\\users.json")
    data = json.load(f)

    try:
        if h.hasUser(user,data):
            user = data['users'][user]
        else:
            print("Error. Coudn't find user: {}".format(user))
            print("Exiting...")
            exit()
    except IOError as error:
        print(error)
        exit()


    username = user['name']
    password = user['password']
    atcud = user['atcud']


    with Firefox(executable_path = path + '\core\Selenium\geckodriver.exe') as driver:
        # Login into e-facturas
        driver.get("https://www.acesso.gov.pt/jsp/loginRedirectForm.jsp?path=registarDocumentoEmitenteForm.action&partID=EFPF")
        nif_span_box = driver.find_element_by_css_selector("label[for='tab2']")
        nif_span_box.click()
        username_box = driver.find_element_by_name("username")
        username_box.send_keys(username)
        password_box = driver.find_element_by_name("password")
        password_box.send_keys(password)
        login_btn = driver.find_element_by_name("sbmtLogin")
        login_btn.click()

        # Insert Faturas
        for fatura in faturas:

            # Validate if Fatura has empty attributes
            if (h.hasEmptyAttribute(fatura)):
                # If it is, skip registry
                print("Fatura {} não introduzida - valores vazios".format(fatura.number))
                continue

            try:                   
                
                driver.get("https://faturas.portaldasfinancas.gov.pt/registarDocumentoEmitenteForm.action")
                
                nif_box = driver.find_element_by_name("nifAdquirente")
                nif_box.send_keys(fatura.nif)
                # nif_box.send_keys("123456789")
                
                number_box = driver.find_element_by_name("numeroDocumento")
                number_box.send_keys(fatura.number)
                # number_box.send_keys("1234")

                atcud_box = driver.find_element(By.ID,"atcud")
                # Form selection shorcut, standf for "Iva - Regime de Isenção Art. 53"
                atcud_box.send_keys(atcud)
                
                doctype_box = driver.find_element_by_name("tipoDocumento")
                doctype_box.send_keys("F")
                
                date_box = driver.find_element_by_name("dataEmissaoDocumento")
                date_box.send_keys(fatura.date)
                # date_box.send_keys("2022-01-12")

                doc_state = driver.find_element_by_name("estadoDocumento")
                doc_state.send_keys("n")

                doc_line = driver.find_element_by_xpath("//a[@onclick=\"editar(this)\"]")
                doc_line.click()

                # -- Line Doc Modal

                select_iva_taxbox = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='taxaIvaVerba']/option[@value='ISE']")))
                select_iva_taxbox.click()

                select_reason_box = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='motivoIsencao']/option[@value='M10']")))
                # Form selection shorcut, stand for "Iva - Regime de Isenção Art. 53"
                select_reason_box.send_keys("M10")

                value_input_box = driver.find_element(By.ID,"totalInput")
                value_input_box.send_keys(fatura.value)

                debit_credit_box = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='debitoCreditoInput']/option[@value='D']")))
                debit_credit_box.click()

                # End Line Doc Modal --

                element = driver.find_element_by_xpath("//div[@class='modal-backdrop fade in']")
                driver.execute_script("arguments[0].style.visibility='hidden'", element)

                confirm_btn = driver.find_element(By.ID,"guardarDetalheLinhaModal")
                confirm_btn.click()

                # End Line Doc
                
                save_btn = driver.find_element(By.ID,"guardarDocumentoBtn")
                save_btn.click()

                # error_box = driver.find_element_by_class_name("alert-error")
                # if error_box != None:
                #     print("Erro ao introduzir a fatura {}".format(fatura.number))

                time.sleep(SECONDS_BETWEEN_FATURAS)

            except IOError as error:
                print(error)
                exit
        
        print("End")




