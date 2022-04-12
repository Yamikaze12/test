from odoo import api, fields, models


class Session(models.Model):
    _name = 'test.session'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True, size=100)
    course_id = fields.Many2one(comodel_name='test.course', string='Course')
    is_instrukturnya = fields.Many2one(comodel_name='res.partner', string='Instruktur')
    start_date = fields.Date(string='Start date', default = fields.Date.today())
    duration = fields.Integer(string='Durasion')
    seats = fields.Integer(string='Seats')
    active = fields.Boolean(string='Is Active', default=True)
    attendee_ids = fields.One2many(comodel_name='test.attendee', inverse_name='session_id', string='Attendee')
    taken_seats = fields.Float(compute='_compute_taken_seats', string='Taken Seats')
    
    
    def _compute_taken_seats(self):
        for x in self:
            if x.seats > 0:
                x.taken_seats = 100.0 * len(x.attendee_ids) / x.seats
            else:
                x.taken_seats = 0.0
    
    @api.onchange('seats')
    def _onchange_seats(self):
        for self in self:
            if self.seats > 0:
                self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
            else:
                self.taken_seats = 0.0
                
    @api.multi
    def _cek_instruktur(self):
        for session in self:
            x = []
            for attendee in session.attendee_ids:
                x.append(attendee.partner_id.id)
            if session.is_instrukturnya.id in x:
                return False
        return True
    _constraints = [(_cek_instruktur,'Instruktur sama',['is_instrukturnya','attendee_ids'])]
    
    
    @api.multi
    def copy(self, default=None):
        """
            Create a new record in Session model from existing one
            @param default: dict which contains the values to be override during
            copy of object
    
            @return: returns a id of newly created record
        """

        default = dict(default or {}, name = self.name + " copy")
        
        result = super(Session, self).copy(default=default)
        
    
        return result
    