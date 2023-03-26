import json
import os.path

import jsonpickle

from model.contact_information import ContactInfo
import random
import string
import re
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=3
f="data/contacts.json"

for o, a in opts:
    if o =="-n":
        n = int(a)
    elif o =="-f":
        f = a
def random_string(prefix, maxlen):
    symbols= string.ascii_letters + string.digits + " "
    name = prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + " "*10
    name = name.replace("'", "")  # remove single quotes
    return re.sub(" {2,}", " ", name).strip()  ## replace multiple whitespaces with one and trim whitespaces



testdata = [ContactInfo(firstname ="", lastname ="", address ="", homephone ="",
                        mobilephone = "", workphone = "", secondaryphone = "", company = "",
                        email = "", email2 = "", email3 = "")] + [
    ContactInfo(firstname =random_string("firstname",10), lastname = random_string("lastname",10), address = random_string("address",20), homephone = random_string("homephone",10),
    mobilephone = random_string("mobilephone",10), workphone =random_string("workphone",10), secondaryphone = random_string("secondaryphone",10), company = random_string("company",20),
    email = random_string("email",20), email2 = random_string("email2",20), email3 = random_string("email3",20))
    for i in range (n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))