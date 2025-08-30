# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResCountryCity(models.Model):
    _name = 'res.country.city'
    _description = "Ciudad"

    _sql_constraints = [
        ('mmd_id_uniq', 'unique(mmd_id)', 'El ID de la Ciudad de MMD debe ser único')
    ]

    name = fields.Char(string="Nombre")
    country_id = fields.Many2one(comodel_name="res.country", string="País")
    mmd_id = fields.Char(string="MMD Pawn - ID Ciudad")
