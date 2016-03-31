
from openerp import fields, models


class Course(models.Model):

    _name = "openacademy.session"
    _description = "Session"

    name = fields.Char(
        string="Name"
    )
    start_date = fields.Date(
        string = "Start Date"
    )
    duration = fields.Integer(
        string = "Duration"
    )
    seats = fields.Integer(
        string = "Seats"
    )
    instructor_id = fields.Many2one('res.partner')
    course_id = fields.Many2one('openacademy.course')

