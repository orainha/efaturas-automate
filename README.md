# efaturas-automate

## 1. About

The portuguese hand-written invoices (Faturas) have to be manualy inserted one by one on the governament portal website ([efacturas](https://faturas.portaldasfinancas.gov.pt])) which it can be pretty annoying if there is many to insert.

The Goal was to automate this process, which is:
- Login into [efacturas](https://faturas.portaldasfinancas.gov.pt])
- Go to "Comerciante"
- Select "Recolher Faturas"
- Fill and Submit a form for each Invoice
- Done

To:
- Fill xlsx spreadsheet with the invoices
- Run script
- Done


## 2. Installation

1. Clone this repository
```shell
git clone https://github.com/orainha/efaturas-automate.git
```
2. Config user credentials on **config/users.json**
```python
{
    "users": 
        {
            "Bob":{
                "name" : "116123032",
                "password" : "B0b78!$@",
                "atcud": "AY6UI4HF"
            },
            "Alice":            {
                "name" : "164812373",
                "password" : "Al1c3#yE",
                "atcud": "BY6IO4PZ"
            }
        }

}
```

3. Install Dependencies
```shell
pip install -r requirements.txt
```



## 3. How to use it

#### 1. Copy your xlxs file to /listagem
- Columns must be: NUMBER | NIF | DATE | VALUE
- Check listagem/example.xlsx for details
#### 2. Go to the folder and run main.py, giving the --user
- The user must be on config/users.json

#### Example:
```shell
cd efaturas-automate
python.exe main.py --user Bob
```

## 4. Notes
**efaturas-automate** it's defined to insert all invoices with 0% IVA (tax).

The code have to changed to accept multiple IVA's:
- The spreeadsheet has to be the IVA field
- The Fatura class has to be the IVA atrribute
- The function 'sheet_to_faturas' and 'hasEmptyAttributes' on helpers.py need to handle IVA field
- The keys sent to 'iva_box' and 'reason_box' have to be handled on selenium.py
 ```python
 # selenium.py
    select_iva_taxbox = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='taxaIvaVerba']/option[@value='ISE']")))
    select_iva_taxbox.click()

    select_reason_box = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='motivoIsencao']/option[@value='M10']")))
    # Form selection shorcut, stand for "Iva - Regime de Isenção Art. 53"
    select_reason_box.click()
 ```

## 5. License
efaturas-automate is available under the terms of the MIT License.
