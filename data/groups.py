from model.group import Group
# import random
# import string
# import re

testdata =[
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + string.punctuation + " "*10  #
#     name = prefix + " ".join([random.choice(symbols) for i in range (random.randrange(maxlen))])
#     name = name.replace("'", "") # remove single quotes
#     return re.sub(" {2,}", " ", name).strip() ## replace multiple whitespaces with one and trim whitespaces
#
#
# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name", 10), header= random_string("header", 20), footer=random_string("footer", 20))
#     for i in range (5)
# ]