import os
import glob
import xlrd3 as xlrd# Reading an excel file using Python
from datetime import datetime

class Fatura:
    def __init__(self,number,nif,date,value):
        
        # validate = [number,nif,date,value]
        # if self.validate(validate):
        self.number = number
        self.nif = nif
        self.date = date
        self.value = value
    
    def validate(list):

        number = list[0]
        nif = list[1]
        date = list[2]
        value = list[3]



def process_excel(fpath):

    if os.path.exists(fpath):
        
        os.chdir(fpath)

        if len(glob.glob(f"*.xlsx")) > 0:

            # Check if document is open
            xlsxFilename = glob.glob(f"*.xlsx")
            xlsxFilename = str(xlsxFilename[0])
            # print(xlsxFilename)
            # for xlsx in xlsxFilename:
            #     if xlsx.find("$") > 0:
            #         # print("ATENÇÃO: Ficheiro Aberto")
            #         # return False
            #         continue

            # # Check if its more than one file to open
            # if (len(xlsxFilename) > 1):
            #     print("ATENÇÃO: EXISTE MAIS DO QUE UM FICHEIRO PARA PROCESSAR")

            # for xlsx in xlsxFilename:
            #     if (len(xlsxFilename) > 1):
            #         print(xlsx)
       
        # To open Workbook
        wb = xlrd.open_workbook(xlsxFilename)
        sheet = wb.sheet_by_index(0)

        return sheet




def sheet_to_faturas(fpath):

    sheet = process_excel(fpath)

    faturas = list()
    for row in range(1,sheet.nrows):
        # # For row 0 and column 0
        # print(sheet.cell_value(row, 0))
        # for col in range(0, sheet.ncols):
            # print(sheet.cell_value(row, col))
        number = int(sheet.cell_value(row, 0))
        nif = int(sheet.cell_value(row, 1))
        sheet_date = sheet.cell_value(row, 2)
        date = datetime(*xlrd.xldate_as_tuple(sheet_date, 0)).date()
        value = float(sheet.cell_value(row, 3))
        
        f = Fatura(number,nif,date,value)
        faturas.append(f)

    # for f in faturas:
    #     print(f.value)

    return faturas


def recolher_fatura_efaturas():
    pass