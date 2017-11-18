# -*- coding: utf-8 -*-
import pytest

from fixture.application2 import Application2
from model.contact2 import Contact


@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session2.login(username="admin", password="secret")
    app.group2.create_contact(Contact(firstname="fghfgthg", lastname="fghgjhgj", address="jgfjgjg", home="gjgjghjhk", email="hgjhjhjkkh"))
    app.session2.logout()

def test_add_empty_contact(app):
    app.session2.login(username="admin", password="secret")
    app.group2.create_contact(Contact(firstname="", lastname="", address="", home="", email=""))
    app.session2.logout()
