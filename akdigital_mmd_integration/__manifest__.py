# -*- coding: utf-8 -*-
{
    'name': 'AK Digital - MMD Integration',
    'version': '18.0.0.7',
    'summary': 'Integración entre Odoo y el sistema de Mas me Dan (MMD)',
    'description': """
        Integración entre Odoo y el sistema de Mas me Dan (MMD)
    """,
    'author': 'AK Digital',
    'contributor': 'Ismael Castillo - ismaonline2000@gmail.com',
    'license': 'LGPL-3',
    'category': 'CRM',
    'depends': ['contacts', 'purchase', 'stock'],
    'data': [
        "data/res_groups.xml",
        "security/ir.model.access.csv",
        "views/product_template.xml",
        "views/res_partner.xml",
        "views/res_country_city.xml",
        "views/res_country_state.xml",
        "views/product_category.xml",
        "views/stock_warehouse.xml"
    ],
    'installable': True,
}
