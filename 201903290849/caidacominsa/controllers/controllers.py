# -*- coding: utf-8 -*-
from odoo import http

# class Caidacominsa(http.Controller):
#     @http.route('/caidacominsa/caidacominsa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caidacominsa/caidacominsa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('caidacominsa.listing', {
#             'root': '/caidacominsa/caidacominsa',
#             'objects': http.request.env['caidacominsa.caidacominsa'].search([]),
#         })

#     @http.route('/caidacominsa/caidacominsa/objects/<model("caidacominsa.caidacominsa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caidacominsa.object', {
#             'object': obj
#         })