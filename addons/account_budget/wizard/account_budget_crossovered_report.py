# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

import time
from gce.osv import fields, osv


class account_budget_crossvered_report(osv.osv_memory):

    _name = "account.budget.crossvered.report"
    _description = "Account Budget crossovered report"
    _columns = {
        'date_from': fields.date('Start of period', required=True),
        'date_to': fields.date('End of period', required=True),
    }
    _defaults = {
        'date_from': lambda *a: time.strftime('%Y-01-01'),
        'date_to': lambda *a: time.strftime('%Y-%m-%d'),
    }

    def check_report(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        data = self.read(cr, uid, ids, context=context)[0]
        datas = {
            'ids': context.get('active_ids', []),
            'model': 'crossovered.budget',
            'form': data
        }
        datas['form']['ids'] = datas['ids']
        datas['form']['report'] = 'analytic-full'
        return self.pool['report'].get_action(cr, uid, [], 'account_budget.report_crossoveredbudget', data=datas, context=context)
