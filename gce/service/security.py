# -*- coding: utf-8 -*-
# Part of clouderp. See LICENSE file for full copyright and licensing details.

import gce
import gce.exceptions

def login(db, login, password):
    res_users = gce.registry(db)['res.users']
    return res_users._login(db, login, password)

def check(db, uid, passwd):
    res_users = gce.registry(db)['res.users']
    return res_users.check(db, uid, passwd)
