# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    _sql_constraints = [
        ('mmd_id_uniq', 'unique(mmd_id)', 'El ID de la Provincia de MMD debe ser único')
    ]

    mmd_id = fields.Char(string="MMD Pawn - ID Provincia")