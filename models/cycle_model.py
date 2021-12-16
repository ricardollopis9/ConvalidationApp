from odoo import models, fields, api

class Cycle_Model(models.Model):
    _name = 'convalidation_app.cycle_model'
    _description = 'Cycle Model'

    name = fields.Char('Cycle Name', required=True)
    description = fields.Text("Description", required = False)

    modules = fields.One2many('convalidation_app.module_model', 'cycle', 'Modules')
