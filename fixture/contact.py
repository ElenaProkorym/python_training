from model.contact_information import ContactInfo
import re
import time
class ContactHelper:

    def __init__(self, app):
        self.app = app

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cache = []
            for tr_element in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = tr_element.find_elements_by_tag_name("td")
                first_name = tr_element.find_element_by_css_selector("td:nth-child(3)").text
                last_name = tr_element.find_element_by_css_selector("td:nth-child(2)").text
                id = tr_element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_email_address = cells[4].text
                address = cells[3].text
                self.contacts_cache.append(ContactInfo(id = id, firstname=first_name, lastname= last_name,\
                                                       all_phones_from_home_page = all_phones,
                                                       address= address,
                                                       all_email_address_from_home_page= all_email_address))
        return list(self.contacts_cache)

    def fill_new_form(self, contact_info):
        wd = self.app.wd
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        # Fill contact form
        # First name
        self.set_first_name(contact_info)
        # Last name
        self.set_last_name(contact_info)
        # fill company
        self.set_company(contact_info)
        # fill address
        self.set_address(contact_info)
        #self.set_secondary_address(contact_info)
        # fill telephone
        self.set_home_phone(contact_info)
        self.set_mobile_phone(contact_info)
        self.set_work_phone(contact_info)
        self.set_secondary_phone(contact_info)
        # fill email address
        self.set_email(contact_info)
        self.set_email_2(contact_info)
        self.set_email_3(contact_info)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        #self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def set_home_phone(self, contact_info):
        if contact_info.homephone is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_info.homephone)

    def set_mobile_phone(self, contact_info):
        if contact_info.mobilephone is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_info.mobilephone)

    def set_work_phone(self, contact_info):
        if contact_info.workphone is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact_info.workphone)

    def set_fax_phone(self, contact_info):
        if contact_info.faxphone is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact_info.faxphone)

    def set_secondary_phone(self, contact_info):
        if contact_info.secondaryphone is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact_info.secondaryphone)

    def set_address(self, contact_info):
        if contact_info.address is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_info.address)

    def set_secondary_address(self, contact_info):
        if contact_info.secondaryaddress is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact_info.secondaryaddress)

    def set_company(self, contact_info):
        if contact_info.company is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_info.company)

    #def click_delete_first_contact(self):
        #self.click_delete_contact()

    def click_delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contacts_cache = None

    def click_add_to_group(self):
        wd = self.app.wd
        group_id = wd.find_element_by_name("to_group").get_attribute("value")
        wd.find_element_by_xpath("//input[@name='add']").click()
        return group_id

    def click_group_page(self):
        wd = self.app.wd
        time.sleep(1)
        wd.find_element_by_xpath("//div[@id='content']/div/i/a").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def click_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.contacts_cache = None

    def click_edit_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php?id="+id+"']").click()
        self.contacts_cache = None

    def click_edit_first_contact(self):
        self.click_edit_contact_by_index(0)

    def click_update_button(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def set_email(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_info.email)

    def set_email_2(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact_info.email2)

    def set_email_3(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact_info.email3)

    def set_first_name(self, contact_info):
        if contact_info.firstname is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_info.firstname)

    def set_last_name(self, contact_info):
        if contact_info.lastname is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_info.lastname)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        #secondaryaddress = wd.find_element_by_name("address2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone= wd.find_element_by_name("home").get_attribute("value")
        workphone= wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return ContactInfo(firstname= firstname, lastname = lastname, id = id, address = address, homephone = homephone, workphone= workphone,
                           mobilephone= mobilephone, secondaryphone = secondaryphone, email = email, email2 = email2, email3 = email3)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        tr_element= wd.find_elements_by_name("entry")[index]
        cell= tr_element.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        tr_element= wd.find_elements_by_name("entry")[index]
        cell= tr_element.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text= wd.find_element_by_id("content").text
        homephone= re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return ContactInfo(homephone= homephone, workphone= workphone, mobilephone= mobilephone, secondaryphone= secondaryphone )