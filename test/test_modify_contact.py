from model.contact import Contact


def test_modify_contact_firstname(app):
        old_contacts = app.contact.get_contact_list()
        app.contact.modify_first_contact(Contact(firstname="New contact"))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)


def test_modify_contact_lastname(app):
        old_contacts = app.contact.get_contact_list()
        app.contact.modify_first_contact(Contact(lastname="New lastname"))
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)

