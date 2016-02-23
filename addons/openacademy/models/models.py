# -*- coding: utf-8 -*-

from openerp import models, fields, api

class openacademy(models.Model):
    _name = 'openacademy.course'

#   Special field
# required for various display and search behavior, can be overridden by setting _rec_name
    name = fields.Char(string="Title", required=True)

    description = fields.Text()

