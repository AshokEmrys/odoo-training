# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

#   Special field
# required for various display and search behavior, can be overridden by setting _rec_name
    name = fields.Char(string="Title", required=True)

    description = fields.Text()

class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of Seats")

