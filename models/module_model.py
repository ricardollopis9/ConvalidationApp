from itertools import cycle
from odoo import models, fields, api


class Module_Model(models.Model):
    _name = 'convalidation_app.module_model'
    _description = 'Module Model'

    name = fields.Char('Module Name', required=True)
    description = fields.Char('Description', required = False)
    hours = fields.Integer('Hours', required = True)
    convalidations = fields.One2many('convalidation_app.convalidation_model', 'module_id', 'Convalidations')
    cycle = fields.Many2one('convalidation_app.cycle_model', 'Cycle')