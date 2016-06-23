# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

import gce

import interface
import print_xml
import print_fnc
import custom
import render
import int_to_text

import report_sxw

import printscreen

def render_report(cr, uid, ids, name, data, context=None):
    """
    Helper to call ``ir.actions.report.xml.render_report()``.
    """
    registry = gce.modules.registry.RegistryManager.get(cr.dbname)
    return registry['ir.actions.report.xml'].render_report(cr, uid, ids, name, data, context)
