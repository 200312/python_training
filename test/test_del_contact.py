from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count1() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.delete_first_contact()
