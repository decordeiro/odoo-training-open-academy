
from openerp import fields, models


class Course(models.Model):

    _name = "openacademy.course"
    _description = "Course"

    name = fields.Char(
        string="Name",
        required=True
    )
    description = fields.Text(
        string="Descricao"
    )
    responsable_id = fields.Many2one('res.users')
    session_id = fields.One2many('openacademy.session', 'id')


