# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

from gce.osv import osv, fields
from gce.tools.translate import _

class note_pad_note(osv.osv):
    """ memo pad """

    _name = 'note.note'
    _inherit = ['pad.common','note.note']

    _pad_fields = ['note_pad']

    _columns = {
        'note_pad_url': fields.char('Pad Url', pad_content_field='memo'),
    }