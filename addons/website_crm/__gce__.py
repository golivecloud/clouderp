{
    'name': 'Contact Form',
    'category': 'Website',
    'website': 'https://www.golive.pt/page/website-builder',
    'summary': 'Create Leads From Contact Form',
    'version': '2.0',
    'description': """
gce Contact Form
====================

        """,
    'depends': ['website_form','website_partner', 'crm'],
    'data': [
        'data/website_crm_data.xml',
        'views/website_crm.xml',
    ],
    'installable': True,
    'auto_install': True,
}
