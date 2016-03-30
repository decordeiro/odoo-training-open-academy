
from openerp import models, fields, api


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

