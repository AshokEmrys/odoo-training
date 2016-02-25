# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

#   Special field
# required for various display and search behavior, can be overridden by setting _rec_name
    name = fields.Char(string="Title", required=True)

    description = fields.Text()

    responsible_id = fields.Many2one('res.users',
            ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of Seats")
    percen_taken_seats = fields.Float(digits=(2,2), string = "Taken Seats", compute='_percen_taken_seats')
    instructor_id = fields.Many2one('res.partner', string='Instructor', domain=['&', '|', ('instructor', '=', True), ('category_id.name', 'ilike', 'Teacher'), ('company_type', '=', 'person')])
    course_id = fields.Many2one('openacademy.course', string="Course", required=True, ondelete='cascade')
    attendee_ids = fields.Many2many('res.partner', string="Attendeed")

    @api.depends('attendee_ids', 'seats')
    @api.one
    def _percen_taken_seats(self):
        if not self.seats:
            self.percen_taken_seats = 0.0
        else:
            self.percen_taken_seats = 100.0 * len(self.attendee_ids) / self.seats

