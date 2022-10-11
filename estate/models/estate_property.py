from odoo import api, fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
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

    total_area = fields.Float(compute="_compute_total_area")
    best_offer = fields.Float(string="Best offer", compute="_compute_best_offer")

    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Sales person", default=lambda self: self.env.user)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    active = fields.Boolean('Active', default=True, help="If unchecked, it will allow you to hide the property without removing it.")
    state = fields.Selection([('new', 'New'), ('offer_received', 'Offer received'), ('sold', 'Sold')], string='Status', default='new', required=True)

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price')) if record.offer_ids else False

    @api.onchange("garden")
    def _onchange_garden(self):
        self.garden_area = 10 if self.garden else (self._origin.garden_area or False)
        self.garden_orientation = 'north' if self.garden else (self._origin.garden_orientation or False)