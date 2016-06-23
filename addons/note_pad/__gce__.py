# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

{
    'name': 'Memos pad',
    'version': '0.1',
    'category': 'Tools',
    'description': """
This module update memos inside gce for using an external pad
=================================================================

Use for update your text memo in real time with the following user that you invite.

""",
    'website': 'https://www.golive.pt/page/notes',
    'summary': 'Sticky memos, Collaborative',
    'depends': [
        'mail',
        'pad',
        'note',
    ],
    'data': [
        'note_pad_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
