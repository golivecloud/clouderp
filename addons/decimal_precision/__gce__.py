# -*- encoding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Decimal Precision Configuration',
    'description': """
Configure the price accuracy you need for different kinds of usage: accounting, sales, purchases.
=================================================================================================

The decimal precision is configured per company.
""",
    'version': '0.1',
    'depends': ['base'],
    'category' : 'Hidden/Dependency',
    'data': [
        'decimal_precision_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
}
