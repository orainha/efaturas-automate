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
                "password" : "B0b78!$@"
            },
            "Alice":            {
                "name" : "164812373",
                "password" : "Al1c3#yE"
            }
        }

}
```

3. Install xlrd3
```shell
pip install xlrd3

#Note:
xlrd3 is required to open and process xlsx spreedsheets
```



## 3. How to use it

Go to the folder and run main.py, giving the --user
##### The user must be on config/users.json

```shell
cd efaturas-automate
python main.py --user Bob
```

## 4. Notes
**efaturas-automate** it's programmed to insert all invoices with 0% IVA (tax).

The code have to changed to accept multiple IVA's:
- The spreeadsheet has to be the IVA field
- The Fatura class has to be the IVA atrribute
- The function 'sheet_to_faturas' and 'hasEmptyAttributes' on helpers.py need to handle IVA field
- The keys sent to 'iva_box' and 'reason_box' have to be handled on selenium.py
 ```python
    iva_box = driver.find_element(By.ID,"tIva_0")
    # Form selection shorcut, stands for "Isento"
    iva_box.send_keys("i")

    reason_box = driver.find_element(By.ID,"motivo_0")
    # Form selection shorcut, standf for "Iva - Regime de Isenção Art. 53"
    reason_box.send_keys("ii")
 ```

## 5. License
efaturas-automate is available under the terms of the MIT License.
