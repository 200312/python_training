import re
from model.contact import Contact

def test_email_on_home_page(app, check_ui):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    if check_ui:
        assert sorted(contact_from_home_page.all_email_from_home_page, key=Contact.id_or_max) == sorted(merge_email_like_on_home_page(contact_from_edit_page), key=Contact.id_or_max)


def test_email_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3

def clear(s):
    return re.sub("[ ]", "", s)

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), [contact.email, contact.email2, contact.email3])))