import re
from model.contact import Contact

def test_address_on_home_page(app, check_ui):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address_from_home_page == merge_address_like_on_home_page(contact_from_edit_page)
    if check_ui:
        assert sorted(contact_from_home_page.address_from_home_page, key=Contact.id_or_max) == sorted(merge_address_like_on_home_page(contact_from_edit_page), key=Contact.id_or_max)


def test_address_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.address == clear(contact_from_edit_page.address)
    assert contact_from_view_page.secondaryaddress == clear(contact_from_edit_page.secondaryaddress)

def clear(s):
    return re.sub("[\n]", "", s)

def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", (map(lambda x: clear(x), [contact.address]))))