from model.group import Group

def test_delete_first_group(app):
    if app.group.count2() == 0:
        app.contact.create_contact(Group(name="test"))
    app.group.delete_first_group()
