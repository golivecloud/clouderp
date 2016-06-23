#-*- coding:utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

from gce.osv import fields, osv
import gce.addons.decimal_precision as dp


class res_company(osv.osv):
    _inherit = 'res.company'

    _columns = {
        'plafond_secu': fields.float('Plafond de la Securite Sociale', digits_compute=dp.get_precision('Payroll')),
        'nombre_employes': fields.integer('Nombre d\'employes'),
        'cotisation_prevoyance': fields.float('Cotisation Patronale Prevoyance', digits_compute=dp.get_precision('Payroll')),
        'org_ss': fields.char('Organisme de securite sociale'),
        'conv_coll': fields.char('Convention collective'),
    }


class hr_contract(osv.osv):
    _inherit = 'hr.contract'

    _columns = {
        'qualif': fields.char('Qualification'),
        'niveau': fields.char('Niveau'),
        'coef': fields.char('Coefficient'),
    }

class hr_payslip(osv.osv):
    _inherit = 'hr.payslip'

    _columns = {
        'payment_mode': fields.char('Mode de paiement'),
    }
