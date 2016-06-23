# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.


{
    'name': 'Point of Sale Discounts',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Simple Discounts in the Point of Sale ',
    'description': """

=======================

This module allows the cashier to quickly give a percentage
sale discount to a customer.

""",
    'depends': ['point_of_sale'],
    'data': [
        'views/views.xml',
        'views/templates.xml'
    ],
    'qweb': [
        'static/src/xml/discount.xml',
    ],
    'installable': True,
    'website': 'https://www.golive.pt/page/point-of-sale',
    'auto_install': False,
}
