# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.
from gce import http
from gce.addons.website_portal.controllers.main import website_account
from gce.http import request


class WebsiteAccount(website_account):
    @http.route(['/my', '/my/home'], type='http', auth="user", website=True)
    def account(self):
        response = super(WebsiteAccount, self).account()
        user = request.env.user
        project_issues = request.env['project.issue'].search([])
        response.qcontext.update({'issues': project_issues})
        return response


class WebsiteProjectIssue(http.Controller):
    @http.route(['/my/issues/<int:issue_id>'], type='http', auth="user", website=True)
    def issues_followup(self, issue_id=None):
        issue = request.env['project.issue'].browse(issue_id)
        return request.website.render("website_project_issue.issues_followup", {'issue': issue})
