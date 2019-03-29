from odoo import models, fields, api
from datetime import datetime



class stock(models.Model):
    _inherit = 'stock.picking'

    def fechadeemi(self):
        # print ('')
        # ho
        a = 'hola'
        b = datetime.now()
        fecha = str(b.year) + '-' + str(b.month) + '-' + str(b.day)
        # fecha = str(b.year) + '-' + str(b.month) + '-' + str(now.day)
        return fecha
