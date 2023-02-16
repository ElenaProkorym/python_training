# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from contact_information import Contactinfo

class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        firefox_binary = FirefoxBinary()
        self.wd = webdriver.Firefox(firefox_binary=firefox_binary)
        self.wd.implicitly_wait(30)
    
    def test_add_new_contact(self):
        wd = self.wd
        # Open home page
        self.open_home_page(wd)
        # Login
        self.login(wd, username = "admin", password = "secret")
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_new_contact_form(wd, Contactinfo(address = "Минск, Беларусь", company = "ZippyBus", firstname = "Елена", home ="224616", lastname = "Прокорым"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        # Return to home page
        wd.find_element_by_link_text("home page").click()

    def fill_new_contact_form(self, wd, contactinfo):
        # Fill contact form
        # First name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contactinfo.firstname)
        # Last name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contactinfo.lastname)
        # fill company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contactinfo.company)
        # fill address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contactinfo.address)
        # fill telephone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contactinfo.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("email").click()
        # Birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys()
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
