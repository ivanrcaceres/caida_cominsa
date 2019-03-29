# -*- coding: utf-8 -*-
from odoo import fields, models, exceptions, api
from odoo import fields, models, exceptions, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from num2words import num2words


class fact2(models.Model):
    _inherit = 'account.invoice'

    def sacacoma(self, n):
        # ho
        return int(n)

    def cortar(self, p):
        b = str(p)
        a = b[0:90]
        return a

    def sacacorchete(self, n):
        a = n.split(" ")
        print(n)
        print(a)
        print(a[-1])
        b = len(a)
        # if(b>0):
        #     return a[1]
        # else:
        #     return a[0]
        return a[-1]


    # funciones para gigi

    # def numerodetalleventa(self):
    #     a = len(self.invoice_line_ids)
    #     print(a)
    #     return

    # def agregar_punto_de_miles(self,numero):
    #     numero_con_punto='.'.join([str(int(numero))[::-1][i:i+3] for i in range(0,len(str(int(numero))),3)])[::-1]
    #     return numero_con_punto

    # def sacacoma(self, n):
    #     return int(n)

    # def sacacorchete(self, n):
    #     a = n.split(" ")
    #     print(n)
    #     print(a)
    #     print(a[-1])
    #     b = len(a)
    #     # if(b>0):
    #     #     return a[1]
    #     # else:
    #     #     return a[0]
    #     return a[-1]


    # funciones para gigi

    def numerodetalleventa(self):
        a = len(self.invoice_line_ids)
        print(a)
        return

    def vercadenaexenta(self, p):
        print('hola')
        print(p)
        # a = p.find("Fiscal Exento")
        a = p.find("Exento")
        print(a)

        aux='nook'
        if(a > -1):
            aux = 'ok'

        print(aux)
        return aux


    def vercadenacinco(self, p):
        print('hola')
        print(p)
        # a = p.find("Fiscal 5%")
        a = p.find("5")

        print(a)

        aux='nook'
        if(a > -1):
            aux = 'ok'

        print(aux)
        return aux

    def vercadenadiez(self, p):
        print('hola')
        print(p)
        # a = p.find("Fiscal 10%")
        a = p.find("10")
        print(a)

        aux='nook'
        if(a > -1):
            aux = 'ok'

        print(aux)
        return aux

    def agregar_punto_de_miles(self,numero):
        numero_con_punto='.'.join([str(int(numero))[::-1][i:i+3] for i in range(0,len(str(int(numero))),3)])[::-1]
        return numero_con_punto

    def calcular_letras(self,numero):
        letras=self.monto_en_letras = num2words(numero, lang='es').upper()
        print('hola mundo desde')
        print(round(4.4))
        print(round(4.5))
        print(round(4.6))
        return letras

    def redondeo(self,n):
        print('hola')
        a = round(n)
        return a

    def get_oc(self,p):
        aux = str(p)
        a = self.env['sale.order'].search([('name', '=', aux)])
        return a.x_studio_field_KreMb
