# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

from gce import api, fields, models


class HrExpenseRefuseWizard(models.TransientModel):

    _name = "hr.expense.refuse.wizard"
    _description = "Hr Expense refuse Reason wizard"

    description = fields.Char(string='Reason', required=True)

    @api.multi
    def expense_refuse_reason(self):
        self.ensure_one()

        context = dict(self._context or {})
        active_ids = context.get('active_ids', [])
        expense = self.env['hr.expense'].browse(active_ids)
        expense.refuse_expenses(self.description)
        return {'type': 'ir.actions.act_window_close'}
