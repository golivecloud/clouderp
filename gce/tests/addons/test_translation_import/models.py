# -*- coding: utf-8 -*-
import gce
from gce.tools.translate import _

class m(gce.osv.orm.TransientModel):
    """ A model to provide source strings.
    """
    _name = 'test.translation.import'

    _columns = {
        'name': gce.osv.fields.char(
            '1XBUO5PUYH2RYZSA1FTLRYS8SPCNU1UYXMEYMM25ASV7JC2KTJZQESZYRV9L8CGB',
            size=32, help='Efgh'),
    }

    _('Ijkl')

    # With the name label above, this source string should be generated twice.
    _('1XBUO5PUYH2RYZSA1FTLRYS8SPCNU1UYXMEYMM25ASV7JC2KTJZQESZYRV9L8CGB')
