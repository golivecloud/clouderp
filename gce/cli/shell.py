# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

import code
import os
import signal
import sys

import gce
from . import Command

def raise_keyboard_interrupt(*a):
    raise KeyboardInterrupt()

class Console(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>"):
        code.InteractiveConsole.__init__(self, locals, filename)
        try:
            import readline
            import rlcompleter
        except ImportError:
            print 'readline or rlcompleter not available, autocomplete disabled.'
        else:
            readline.set_completer(rlcompleter.Completer(locals).complete)
            readline.parse_and_bind("tab: complete")

class Shell(Command):
    """Start clouderp in an interactive shell"""
    def init(self, args):
        gce.tools.config.parse_config(args)
        gce.cli.server.report_configuration()
        gce.service.server.start(preload=[], stop=True)
        signal.signal(signal.SIGINT, raise_keyboard_interrupt)

    def console(self, local_vars):
        if not os.isatty(sys.stdin.fileno()):
            exec sys.stdin in local_vars
        else:
            if 'env' not in local_vars:
                print 'No environment set, use `clouderp.py shell -d dbname` to get one.'
            for i in sorted(local_vars):
                print '%s: %s' % (i, local_vars[i])
            Console(locals=local_vars).interact()

    def shell(self, dbname):
        local_vars = {
            'gce': gce
        }
        with gce.api.Environment.manage():
            if dbname:
                registry = gce.modules.registry.RegistryManager.get(dbname)
                with registry.cursor() as cr:
                    uid = gce.SUPERUSER_ID
                    ctx = gce.api.Environment(cr, uid, {})['res.users'].context_get()
                    env = gce.api.Environment(cr, uid, ctx)
                    local_vars['env'] = env
                    local_vars['self'] = env.user
                    self.console(local_vars)
            else:
                self.console(local_vars)

    def run(self, args):
        self.init(args)
        self.shell(gce.tools.config['db_name'])
        return 0
