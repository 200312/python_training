# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="fghfgthg", lastname="fghgjhgj", address="jgfjgjg", home="gjgjghjhk", email="hgjhjhjkkh"))

def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstname="", lastname="", address="", home="", email=""))
