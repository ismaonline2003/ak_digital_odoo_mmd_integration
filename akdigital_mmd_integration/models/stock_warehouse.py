# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    _sql_constraints = [
        ('mmd_id_uniq', 'unique(mmd_id)', 'El ID Almacen de MMD debe ser único')
    ]

    mmd_id = fields.Char(string="MMD - ID Almacen")