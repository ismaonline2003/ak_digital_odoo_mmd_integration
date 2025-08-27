# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _sql_constraints = [
        ('mmd_id_uniq', 'unique(mmd_id)', 'El ID Producto de MMD debe ser único')
    ]

    mmd_id = fields.Char(string="MMD - ID Producto")