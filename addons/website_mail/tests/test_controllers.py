# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

from gce.addons.mail.tests.common import TestMail
from gce.addons.website_mail.controllers.main import WebsiteMail
from gce.tools import mute_logger, email_split


class TestControllers(TestMail):

    def test_00_subscribe(self):
        # from gce.addons.web.http import request
        # print request

        cr, uid = self.cr, self.uid
        # context = { }
        # email = 'Marcel Dupuis <marcel.dupuis@example.com>'
        # website_mail = WebsiteMail()

        # pid = website_mail._find_or_create_partner(email, context)
        # partner = self.res_partner.browse(cr, uid, pid)
        # print partner.name, partner.email
