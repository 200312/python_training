import re

def test_lastname_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname_from_home_page == merge_lastname_like_on_home_page(contact_from_edit_page)

def test_lastname_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname

def clear(s):
    return re.sub("[\n]", "", s)

def merge_lastname_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", (map(lambda x: clear(x), [contact.lastname]))))
