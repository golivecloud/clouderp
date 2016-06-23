# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

""" Regroup variables for deprecated features.

To keep the gce server backward compatible with older modules, some
additional code is needed throughout the core library. This module keeps
track of those specific measures by providing variables that can be unset
by the user to check if her code is future proof.

In a perfect world, all these variables are set to False, the corresponding
code removed, and thus these variables made unnecessary.
"""

# If True, the Python modules inside the gce namespace are made available
# without the 'gce.' prefix. E.g. gce.osv.osv and osv.osv refer to the
# same module.
# Introduced around 2011.02.
# Change to False around 2013.02.
open_gce_namespace = False

# If True, gce.netsvc.LocalService() can be used to lookup reports or to
# access gce.workflow.
# Introduced around 2013.03.
# Among the related code:
# - The gce.netsvc.LocalService() function.
# - The gce.report.interface.report_int._reports dictionary.
# - The register attribute in gce.report.interface.report_int (and in its
# - auto column in ir.actions.report.xml.
# inheriting classes).
allow_local_service = True

# Applies for the register attribute in gce.report.interface.report_int.
# See comments for allow_local_service above.
# Introduced around 2013.03.
allow_report_int_registration = True

# If True, the functions in gce.pooler can be used.
# Introduced around 2013.03 (actually they are deprecated since much longer
# but no warning was dispayed in the logs).
gce_pooler = True
