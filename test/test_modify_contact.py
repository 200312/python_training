from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count2 == 0:
        app.contact.create(Contact(firstname="test"))
        app.contact.modify_first_contact(Contact(firstname="New contact"))

def test_modify_contact_lastname(app):
        app.contact.create(Contact(firstname="test"))
        app.contact.modify_first_contact(Contact(lastname="New lastname"))
