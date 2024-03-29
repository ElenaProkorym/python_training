import re
from turtle import clear
from model.contact_information import ContactInfo


def test_contact_info_on_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert sorted(contacts_from_home_page, key=ContactInfo.id_or_max) == sorted(contacts_from_db,key=ContactInfo.id_or_max)


def test_contact_info_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

    assert contact_from_home_page.all_email_address_from_home_page == merge_email_address_info_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address

def clear(s):
    return re.sub("[() -]","", s)


# def merge_phones_like_on_db(db):
#     # return merge([contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        [db.homephone, db.mobilephone, db.workphone,
#                                         db.phone2]))))

def merge_email_address_info_like_on_home_page(contact):
    #return merge([contact.email, contact.email2, contact.email3])
    name= "\n".join(filter(lambda x: x!="" and x is not None,
                                        [contact.email, contact.email2, contact.email3]))
    return re.sub(" {2,}", " ", name).strip()  ## replace multiple whitespaces with one and trim whitespaces



def merge_phones_like_on_home_page(contact):
    # return merge([contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone])
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

# def merge(items):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        items))))