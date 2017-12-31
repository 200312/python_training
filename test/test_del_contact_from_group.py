# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_contact_from_group(app, db, check_ui):
    old_contacts = db.get_contact_list()
    app.contact.delete_contact_from_group()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
