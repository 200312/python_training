# -*- coding: utf-8 -*-
from model.contact2 import Contact


def test_add_contact(app):
    app.session2.login(username="admin", password="secret")
    app.group2.create_contact(Contact(firstname="fghfgthg", lastname="fghgjhgj", address="jgfjgjg", home="gjgjghjhk", email="hgjhjhjkkh"))
    app.session2.logout()

def test_add_empty_contact(app):
    app.session2.login(username="admin", password="secret")
    app.group2.create_contact(Contact(firstname="", lastname="", address="", home="", email=""))
    app.session2.logout()
