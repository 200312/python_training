import re
from model.contact import Contact


def test_lastname_on_home_page(app, check_ui):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == merge_lastname_like_on_home_page(contact_from_edit_page)
    if check_ui:
        assert sorted(contact_from_home_page.lastname, key=Contact.id_or_max) == sorted(merge_lastname_like_on_home_page(contact_from_edit_page), key=Contact.id_or_max)


def test_lastname_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname

def clear(s):
    return re.sub("[ -]", "", s)

def merge_lastname_like_on_home_page(contact):
    return "\n".join(map(lambda x: clear(x), [contact.lastname]))