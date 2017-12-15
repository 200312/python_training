import re

def test_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.secondaryaddress == clear(contact_from_edit_page.secondaryaddress)

def test_address_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.address == clear(contact_from_edit_page.address)
    assert contact_from_view_page.secondaryaddress == clear(contact_from_edit_page.secondaryaddress)

def clear(s):
    return re.sub("[\n]", "", s)




