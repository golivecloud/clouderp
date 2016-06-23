# -*- coding: utf-8 -*-
{
    'name': 'test-import-export',
    'version': '0.1',
    'category': 'Tests',
    'description': """A module to test import/export.""",
    'author': 'gce SA',
    'maintainer': 'gce SA',
    'website': 'http://www.gce.com',
    'depends': ['base'],
    'data': ['ir.model.access.csv'],
    'installable': True,
    'auto_install': False,
    'test': [
        'tests/test_import_reference.yml',
        'tests/test_import_menuitem.yml',
    ]
}
