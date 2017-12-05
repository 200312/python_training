# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Contact(firstname="fghfgthg", lastname="fghgjhgj", address="jgfjgjg", home="gjgjghjhk", email="hgjhjhjkkh"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


#def test_add_empty_contact(app):
   # app.contact.create_contact(Contact(firstname="", lastname="", address="", home="", email=""))
