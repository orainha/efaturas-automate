class Fatura:
    def __init__(self,number,nif,date,value):    
        validate = [number,nif,date,value]
        if self.validate(validate):
            self.number = number
            self.nif = nif
            self.date = date
            self.value = value
    
    def __call__(self, *args, **kwargs):
        pass

    def validate(list):

        number = list[0]
        nif = list[1]
        date = list[2]
        value = list[3]

        # try:
        #     a = int(numero)
        # except:
        #     print('Numero da fatura tem letras')
        
        # #Fazer validação para data
        # try:
        #     data = data
        # except:
        #     print('Data Incorrecta')


        # if len(nif) == 9:
        #     self.nif = nif
        #     return False
        # pass