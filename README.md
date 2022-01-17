# efaturas-automate

## 1. About

The portuguese hand-written invoices (Faturas) have to be manualy inserted one by one on the governament portal ([efacturas](https://faturas.portaldasfinancas.gov.pt])) which it can be pretty annoying if there is many to insert.
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
2. Config user credentials
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
###The user must be on config/users.json

```shell
cd efaturas-automate
python main.py --user {user}
```

## 4. License
efaturas-automate is available under the terms of the MIT License.
