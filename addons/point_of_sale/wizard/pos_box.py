
from gce.osv import osv
from gce.tools.translate import _
from gce.exceptions import UserError

from gce.addons.account.wizard.pos_box import CashBox

class PosBox(CashBox):
    _register = False

    def run(self, cr, uid, ids, context=None):
        if not context:
            context = dict()

        active_model = context.get('active_model', False) or False
        active_ids = context.get('active_ids', []) or []

        if active_model == 'pos.session':
            records = self.pool[active_model].browse(cr, uid, active_ids, context=context)
            bank_statements = [record.cash_register_id for record in records if record.cash_register_id]

            if not bank_statements:
                raise UserError(_("There is no cash register for this PoS Session"))

            return self._run(cr, uid, ids, bank_statements, context=context)
        else:
            return super(PosBox, self).run(cr, uid, ids, context=context)

class PosBoxIn(PosBox):
    _inherit = 'cash.box.in'

    def _calculate_values_for_statement_line(self, cr, uid, id, record, context=None):
        
        if context is None:
            context = {}
    
        values = super(PosBoxIn, self)._calculate_values_for_statement_line(cr, uid, id, record, context=context)[0]

        active_model = context.get('active_model', False) or False
        active_ids = context.get('active_ids', []) or []

        if active_model == 'pos.session':
            session = self.pool[active_model].browse(cr, uid, active_ids, context=context)[0]
            values['ref'] = session.name

        return values


class PosBoxOut(PosBox):
    _inherit = 'cash.box.out'

    def _calculate_values_for_statement_line(self, cr, uid, id, record, context=None):
        values = super(PosBoxOut, self)._calculate_values_for_statement_line(cr, uid, id, record, context=context)[0]

        active_model = context.get('active_model', False) or False
        active_ids = context.get('active_ids', []) or []

        if active_model == 'pos.session':
            session = self.pool[active_model].browse(cr, uid, active_ids, context=context)[0]
            values['ref'] = session.name

        return values
