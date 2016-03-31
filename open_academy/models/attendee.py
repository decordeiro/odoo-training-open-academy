
from openerp import fields, models


class Course(models.Model):

    _name = "openacademy.attendee"
    _description = "Attendee"

    name = fields.Char(
        string="Name"
    )
    partner_id = fields.Many2one('res.partner')
    session_id = fields.Many2one('openacademy.session')