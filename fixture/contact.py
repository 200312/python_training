
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    #def open_home_page(self):
        #wd = self.app.wd
        #if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//div[@id='content']/form[2]/div[1]/input")) > 0):
            #wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    #def fill_contact_form(self, contact):
        #wd = self.app.wd
        #self.change_field_value("firstname", contact.firstname)
        #self.change_field_value("lastname", contact.lastname)
        #self.change_field_value("home", contact.home)
        #self.change_field_value("mobile", contact.mobile)
        #self.change_field_value("work", contact.work)
        #self.change_field_value("fax", contact.fax)


    #def create_contact(self, contact):
        #wd = self.app.wd
        #self.open_home_page()
        # init contact creation
       # wd.find_element_by_xpath("//div/div[3]/ul/li[2]/a").click()
        #self.fill_contact_form(contact)
        # submit contact creation
        #wd.find_element_by_name("submit").click()
        #self.return_to_home_page()
        #self.contact_cache = None

   # def select_first_contact(self):
        #wd = self.app.wd
        #wd.find_element_by_name("selected[]").click()

    #def select_contact_by_index(self, index):
        #wd = self.app.wd
        #wd.find_elements_by_name("selected[]")[index].click()

    #def delete_first_contact(self):
        #self.delete_contact_by_index(0)

    #def delete_contact_by_index(self, index):
        #wd = self.app.wd
        #self.open_home_page()
        #self.select_contact_by_index(index)
        # submit deletion
        #wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #wd.switch_to_alert().accept()
        #self.return_to_home_page()
        #self.contact_cache = None

    #def modify_first_contact(self):
        #self.modify_contact_by_index(0)

    #def modify_contact_by_index(self, index, new_contact_data):
        #wd = self.app.wd
        #self.open_home_page()
        #self.select_contact_by_index(index)
        # open modification form
       # wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        #self.fill_contact_form(new_contact_data)
        # submit modification
        #wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        #self.return_to_home_page()
        #self.contact_cache = None

    #def return_to_home_page(self):
        #wd = self.app.wd
        #wd.find_element_by_link_text("home").click()

    #def count(self):
        #wd = self.app.wd
        #self.open_home_page()
        #return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, homephone=all_phones[0], mobilephone=all_phones[1], workphone=all_phones[2], fax=all_phones[3], secondaryphone=all_phones[4]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_css_selector("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_css_selector("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id ").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone, mobilephone=mobilephone, fax=fax, secondaryphone=secondaryphone)














