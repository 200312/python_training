# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_to_group(app, db, contact):
    old_contacts = db.get_contact_list()
    app.contact.add_contact_to_group(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)