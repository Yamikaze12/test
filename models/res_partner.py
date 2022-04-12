from odoo import _, api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

is_instrukturnya = fields.Boolean(string='Is Instruktur', default=False)
