# -*- encoding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.
{
    'name': 'Belgium - Payroll with Accounting',
    'category': 'Localization',
    'depends': ['l10n_be_hr_payroll', 'hr_payroll_account', 'l10n_be'],
    'version': '1.0',
    'description': """
Accounting Data for Belgian Payroll Rules.
==========================================
    """,

    'auto_install': True,
    'website': 'https://www.golive.pt/page/accounting',
    'demo': [],
    'data':[
        'l10n_be_hr_payroll_account_data.xml',
    ],
    'post_init_hook': '_set_accounts',
    'installable': True
}
