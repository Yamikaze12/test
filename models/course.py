from odoo import api, fields, models


class Course(models.Model):
    _name = 'test.course'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    deskripsi = fields.Char(string='Deskripsi')
    responsible_id = fields.Many2one(comodel_name='res.users', string='Responsible', required=True)
    
    session_ids = fields.One2many(comodel_name='test.session', inverse_name='course_id', string='Session')
    
    _sql_constrains = [
        ('sql_cek_name','UNIQUE(name)','nama tidak boleh sama')
    ]
