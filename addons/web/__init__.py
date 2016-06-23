import sys

# Mock deprecated gce.addons.web.http module
import gce.http
sys.modules['gce.addons.web.http'] = gce.http
http = gce.http

import controllers
