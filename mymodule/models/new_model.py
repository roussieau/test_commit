from odoo import fields, models

class NewModel(models.Model):
    _name = 'new.model'

    field1 = fields.Char()
    field2 = fields.Char()
