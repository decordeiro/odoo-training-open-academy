from openerp import models, fields, api


class Modelo(models.Model):

    _name = "modelo.modelo"
    _description = "Modelo Base"

    name = fields.Char(
        string="Nome"
    )
    description = fields.Text(
        string="Descricao"
    )
