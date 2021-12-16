import random
import string
from odoo import models, fields, api


class Alumn_Model(models.Model):
    _name = 'convalidation_app.alumn_model'
    _description = 'Alumn model'

    name = fields.Char('Alumn Name', required=True)
    password = fields.Char('Password', required = True)
    photo = fields.Binary('Image', required = False)
    age = fields.Integer('Age', required = True)
    locality = fields.Char('Locaity', required = True)
    province = fields.Char('Province', required = True)
    email = fields.Char('Email', requiired = True)

    convalidations = fields.One2many('convalidation_app.convalidation_model', 'alumn_id', 'Convalidations')

    def genPassword(self):
        self.ensure_one()
        self.password = ''.join(random.choice(string.printable)for i in range(8))