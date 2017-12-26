from model.contact import Contact
import random

def test_modify_contact_firstname(app, db, check_ui):
     if len(db.get_contact_list()) == 0:
            app.contact.create_contact(Contact(firstname="firstname"))
     old_contacts = db.get_contact_list()
     contact = random.choice(old_contacts)
     app.contact.modify_contact_by_id(contact.id)
     new_contacts = db.get_contact_list()
     assert len(old_contacts) == len(new_contacts)
     old_contacts.remove(contact)
     if check_ui:
             assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



#def test_modify_contact_lastname(app):
        #old_contacts = app.contact.get_contact_list()
        #app.contact.modify_first_contact(Contact(lastname="New lastname"))
        #new_contacts = app.contact.get_contact_list()
        #assert len(old_contacts) == len(new_contacts)

