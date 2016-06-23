# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

""" Addons module.

This module serves to contain all gce addons, across all configured addons
paths. For the code to manage those addons, see gce.modules.

Addons are made available under `gce.addons` after
gce.tools.config.parse_config() is called (so that the addons paths are
known).

This module also conveniently reexports some symbols from gce.modules.
Importing them from here is deprecated.

"""
