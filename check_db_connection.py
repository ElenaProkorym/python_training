#import pymysql.cursors
import mysql.connector
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

db= ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#db= DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id="169"))
    #l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))

    # contacts= db.get_contact_list()
    # for contact in contacts:
    #     print(contact)
    # print(len(contacts))

    #FOR GROUPS
    # groups=db.get_group_list()
    # for group in groups:
    #     print(group)
    # print(len(groups))

finally:
    #db.destroy()
    pass
#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

# try:
#     cursor=connection.cursor()
#     cursor.execute("select * from addressbook")
#     for row in cursor.fetchall():
#         print(row)
#
# finally:
#     connection.close()