# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

from gce.osv import osv
from gce.tools.translate import _
from gce.tools.safe_eval import safe_eval as eval
from gce.exceptions import UserError


class crm_lead(osv.osv):
    _inherit = 'crm.lead'

    def get_interested_action(self, cr, uid, interested, context=None):
        try:
            model, action_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'crm_partner_assign', 'crm_lead_channel_interested_act')
        except ValueError:
            raise UserError(_("The CRM Channel Interested Action is missing"))
        action = self.pool[model].read(cr, uid, [action_id], context=context)[0]
        action_context = eval(action['context'])
        action_context['interested'] = interested
        action['context'] = str(action_context)
        return action

    def case_interested(self, cr, uid, ids, context=None):
        return self.get_interested_action(cr, uid, True, context=context)

    def case_disinterested(self, cr, uid, ids, context=None):
        return self.get_interested_action(cr, uid, False, context=context)

    def assign_salesman_of_assigned_partner(self, cr, uid, ids, context=None):
        salesmans_leads = {}
        for lead in self.browse(cr, uid, ids, context=context):
            if (lead.stage_id.probability > 0 and lead.stage_id.probability < 100) or lead.stage_id.sequence == 1: 
                if lead.partner_assigned_id and lead.partner_assigned_id.user_id and lead.partner_assigned_id.user_id != lead.user_id:
                    salesman_id = lead.partner_assigned_id.user_id.id
                    if salesmans_leads.get(salesman_id):
                        salesmans_leads[salesman_id].append(lead.id)
                    else:
                        salesmans_leads[salesman_id] = [lead.id]
        for salesman_id, lead_ids in salesmans_leads.items():
            salesteam_id = self.on_change_user(cr, uid, lead_ids, salesman_id, context=None)['value'].get('team_id')
            self.write(cr, uid, lead_ids, {'user_id': salesman_id, 'team_id': salesteam_id}, context=context)
