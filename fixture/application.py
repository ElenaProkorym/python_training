from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
class Application:
    def __init__(self):
        firefox_binary = FirefoxBinary()
        self.wd = webdriver.Firefox(firefox_binary=firefox_binary)
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)




    def fill_new_contact_form(self, contactinfo):
        wd = self.wd
        # Add new contact
        wd.find_element_by_link_text("add new").click()
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
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def destroy(self):
        self.wd.quit()