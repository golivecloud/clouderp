# -*- encoding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.
#    Coded by: Alejandro Negrin anegrin@vauxoo.com,
#    Planified by: Alejandro Negrin, Humberto Arocha, Moises Lopez
#    Finance by: Vauxoo.
#    Audited by: Humberto Arocha (hbto@vauxoo.com) y Moises Lopez (moylop260@vauxoo.com)
# Part of clouderp. See LICENSE file for full copyright and licensing details.

{
    "name": "Mexico - Accounting",
    "version": "2.0",
    "author": "Vauxoo",
    "category": "Localization/Account Charts",
    "description": """
Minimal accounting configuration for Mexico.
============================================

This Chart of account is a minimal proposal to be able to use OoB the
accounting feature of gce.

This doesn't pretend be all the localization for MX it is just the minimal
data required to start from 0 in mexican localization.

This modules and its content is updated frequently by gce-mexico team.

With this module you will have:

 - Minimal chart of account tested in production eviroments.
 - Minimal chart of taxes, to comply with SAT_ requirements.

.. SAT: http://www.sat.gob.mx/
    """,
    "depends": ["account", "base_vat"],
    "demo_xml": [],
    "data": [
        "data/account_chart.xml",
        "data/account_tax.xml",
        "data/account_chart_template.yml",
    ],
    "installable": True,
    "certificate": False,
}
