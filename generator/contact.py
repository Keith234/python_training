import jsonpickle
import os.path

from model.contact import Contact
import random
import string
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middlename="", lastname="", nicknam="",
                    title="", company="", address="", home="",
                    mobile="", work="", fax="", secondaryphone="",
                    email="", email2="",
                    email3="")] + \
           [Contact(first_name=random_string("first_name", 8), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 11), nicknam=random_string("nicknam", 5),
                    title=random_string("title", 4), company=random_string("company", 12),
                    address=random_string("address", 25), home=random_string("home", 7),
                    mobile="045364636363", work="64646464", fax="85463543", secondaryphone="5364",
                    email=random_string("email", 10), email2=random_string("email2", 10),
                    email3=random_string("email3", 10))
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
