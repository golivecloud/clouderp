# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.


{
    'name': 'Website CRM Claim',
    'version': '0.2',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds claim menu and features to your portal if claim and portal are installed.
==========================================================================================
    """,
    'depends': ['crm_claim','portal', 'website'],
    'data': [
        'portal_claim_view.xml',
        'website_claim_view.xml',
        'security/ir.model.access.csv',
        'security/portal_security.xml',
    ],
    'installable': True,
    'auto_install': True,
    'category': 'Hidden',
}
