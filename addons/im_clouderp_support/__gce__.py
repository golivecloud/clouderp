{
    'name' : 'clouderp Live Support',
    'version': '1.0',
    'summary': 'Chat with the clouderp collaborators',
    'category': 'Tools',
    'complexity': 'medium',
    'website': 'https://www.golive.pt/',
    'description':
        """
clouderp Live Support
=================

Ask your functional question directly to the clouderp Operators with the livechat support.

        """,
    'data': [
        "views/im_clouderp_support.xml"
    ],
    'depends' : ["web", "mail"],
    'qweb': [
        'static/src/xml/im_clouderp_support.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
