from odoo import models, fields, api
from datetime import datetime



class ticket(models.Model):
    _inherit = 'mrp.production'

    def hola(self):
        return 'hola'

    def nombre01(self):
        a = self.product_id.display_name
        b = a.split("]")
        c= b[-1]
        d= c[0:60]
        return d

    def fechadeemi(self):
        # print ('')
        # ho
        a = 'hola'
        b = datetime.now()

        # mes = int(b.month)
        # mes2 = ''
        #
        # if(mes == 1):
        #     mes2 = '1'
        # if (mes == 2):
        #     mes2 = '2'
        # if (mes == 3):
        #     mes2 = '3'
        # if (mes == 4):
        #     mes2 = '4'
        # if (mes == 5):
        #     mes2 = '5'
        # if (mes == 6):
        #     mes2 = '6'
        # if (mes == 7):
        #     mes2 = '7'
        # if (mes == 8):
        #     mes2 = '8'
        # if (mes == 9):
        #     mes2 = '9'
        # if (mes == 10):
        #     mes2 = '10'
        # if (mes == 11):
        #     mes2 = '11'
        # if (mes == 12):
        #     mes2 = '12'


        fecha = str(b.year) + '-' + str(b.month) + '-' + str(b.day)
        # fecha = str(b.year) + '-' + str(b.month) + '-' + str(now.day)
        # fecha = str(b.year) + '-' + mes2 + '-' + str(b.day)
        return fecha
