# -*- coding: utf-8 -*-
from odoo import models, fields, api

class UomUom(models.Model):
    _inherit = 'uom.uom'

    _sql_constraints = [
        ('mmd_id_uniq', 'unique(mmd_id)', 'El ID de la Unidad de Medida de MMD debe ser único')
    ]

    mmd_id = fields.Char(string="MMD - ID Unidad Medida")