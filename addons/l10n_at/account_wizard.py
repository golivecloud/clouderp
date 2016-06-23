# -*- encoding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

# Copyright (C) conexus.at

from gce import tools
from gce.osv import osv
from gce import addons

class AccountWizard_cd(osv.osv_memory):
	_inherit='wizard.multi.charts.accounts'
	
	_defaults = {
		'code_digits' : 0,
	}
