# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [
        ('mmd_id_uniq', 'unique(mmd_id)', 'El ID Contacto de MMD debe ser único')
    ]

    mmd_id = fields.Char(string="MMD - ID Contacto")