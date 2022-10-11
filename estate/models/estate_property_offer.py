from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offer model"

    price = fields.Float(string='Price')
    status = fields.Selection(string='Status',selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)

    validity = fields.Integer(string="Offer validity", default=7)
    date_deadline = fields.Date(string='Offer deadline', compute="_compute_date_deadline", inverse="_compute_validity")
    @api.depends("create_date", "date_deadline")
    def _compute_validity(self):
        for record in self:
            create_date = fields.Date.today() if not record.create_date else record.create_date.date()
            date_deadline = fields.Date.today() if not record.date_deadline else record.date_deadline
            delta = date_deadline - create_date
            record.validity = delta.days

    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            create_date = fields.Date.today() if not record.create_date else record.create_date.date()
            record.date_deadline = fields.Datetime.add(create_date, days=record.validity)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            property = self.env['estate.property'].browse(vals['property_id'])

            if (vals['price'] <= property.best_offer):
                raise UserError(_("Price must be higher than %s", property.best_offer))

            property.state = 'offer_received'

        return super().create(vals_list)