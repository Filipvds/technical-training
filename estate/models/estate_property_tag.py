from odoo import fields, models

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate property tag model"

    name = fields.Char(string='Name', required=True)