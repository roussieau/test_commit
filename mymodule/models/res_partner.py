from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    new_field = fields.Char()
    new_field_2 = fields.Char()
