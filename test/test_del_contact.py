

def test_delete_first_contact(app):
    app.session2.login(username="admin", password="secret")
    app.group2.delete_first_contact()
    app.session2.logout()
