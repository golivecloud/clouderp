# -*- coding: utf-8 -*-
# Copyright: 2014 - gce S.A. <http://gce.com>
import types

def post_mortem(config, info):
    if config['debug_mode'] and isinstance(info[2], types.TracebackType):
        try:
            import pudb as pdb
        except ImportError:
            try:
                import ipdb as pdb
            except ImportError:
                import pdb
        pdb.post_mortem(info[2])
