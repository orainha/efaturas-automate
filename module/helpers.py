import os
import glob
import xlrd3 as xlrd# Reading an excel file using Python
from datetime import datetime

class Fatura:
    """ Fatura is the portuguese translation of an Invoice. """
    def __init__(self,number,nif,date,value):
        self.number = number
        self.nif = nif
        self.date = date
        self.value = value


def process_excel(fpath):
    """ Open xlsx file and return a matrix (with multiple rows and columns) """

    if os.path.exists(fpath):

        os.chdir(fpath)

        # If there is any xlsx files...
        if len(glob.glob(f"*.xlsx")) > 0:

            # Get xlsx file, whatever its name
            xlsxFilenames = glob.glob(f"*.xlsx")
            xlsxFilename = str(xlsxFilenames[0])

            # Check if document is open
            # if xlsxFilename.find("$") > 0:
            #     print("WARNING: File is Open {}".format(xlsxFilename))
            #     exit

            # Check if its more than one file to open
            # if (len(xlsxFilenames) > 1):
            #     print("WARNING: There is more than one file to process.")
            #     for xlsx in xlsxFilenames:
            #         if (len(xlsx) > 1):
            #             print(xlsx)
       
            # Open Workbook using xlrd
            try:
                wb = xlrd.open_workbook(xlsxFilename)
                sheet = wb.sheet_by_index(0)
            except IOError as error:
                print(error)
            finally:
                return sheet
        else:
            print("There is no xlsx files to process. Exiting...")
            exit




def sheet_to_faturas(sheet):
    """ Convert each xlsx sheet row to object of type Fatura, and save into a list """

    faturas = list()
    for row in range(1,sheet.nrows):
        # Debug sheet
        # # For row 0 and column 0
        # print(sheet.cell_value(row, 0))
        # for col in range(0, sheet.ncols):
            # print(sheet.cell_value(row, col))
        try:
            number = str(sheet.cell_value(row, 0)).split('.')[0]
            nif = str(sheet.cell_value(row, 1)).split('.')[0]
            sheet_date = sheet.cell_value(row, 2)
            date = ""
            if sheet_date != "":
                date = str(datetime(*xlrd.xldate_as_tuple(sheet_date, 0)).date())
            value = str(sheet.cell_value(row, 3)).replace('.',',')
        except IOError as error:
            print(error)
            exit
        
        f = Fatura(number,nif,date,value)
        faturas.append(f)

    return faturas


def get_faturas(fpath):
    """ Get Faturas giving the file path only """
    # Give path to get sheet
    sheet = process_excel(fpath)
    # Give sheet to get list of faturas
    faturas = sheet_to_faturas(sheet)
    
    return faturas


def hasEmptyAttribute(fatura):
    """ Find Empty attributes of a Fatura """
    isEmpty = False
    if fatura.nif == "":
        isEmpty = True
    elif fatura.number == "":
        isEmpty = True
    elif fatura.date == "":
        isEmpty = True
    elif fatura.value == "":
        isEmpty = True
    return isEmpty