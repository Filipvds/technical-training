from odoo import fields, models

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate property type model"

    name = fields.Char(string='Name', required=True)