from openerp import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean("Instructor", default=False)

    instructor_session_ids = fields.One2many('openacademy.session', 'instructor_id', string="Instructed Sessions")

    attendee_session_ids = fields.Many2many('openacademy.session', string="Attended Sessions",
            readonly=True)
