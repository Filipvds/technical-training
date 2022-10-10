from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Poscode')
    date_availability = fields.Date(string='Date available')
    expected_price = fields.Float(string='Expected price', required=True)
    selling_rpice = fields.Float(string='Selling price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living area')
    facades = fields.Integer(string='# Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden area')
    garden_orientation = fields.Selection(string='Orientation',selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')])