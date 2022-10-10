from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Poscode')
    date_availability = fields.Date(string='Date available', default=lambda self: fields.Datetime.add(fields.Datetime.now(), months=3), copy=False)
    expected_price = fields.Float(string='Expected price', required=True)
    selling_price = fields.Float(string='Selling price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living area')
    facades = fields.Integer(string='# Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden area')
    garden_orientation = fields.Selection(string='Orientation',selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')])