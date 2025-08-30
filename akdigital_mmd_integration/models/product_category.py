# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = 'product.category'

    _sql_constraints = [
        ('mmd_id_uniq', 'unique(mmd_id)', 'El ID Contacto de MMD debe ser único')
    ]

    mmd_id = fields.Char(string="MMD Pawn - ID")
