from odoo import models, fields, api

class Convalidation_Model(models.Model):
    _name = 'convalidation_app.convalidation_model'
    _description = 'Convalidation Model'

    date = fields.Date('Date', required = True)
    module_id = fields.Many2one('convalidation_app.module_model', 'Module')
    alumn_id = fields.Many2one('convalidation_app.alumn_model', 'Alumn')
