import random
import string
from model.contact import New_contact
import os.path
import jsonpickle
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
    symbols = string.ascii_letters + string.digits + string.punctuation + " " *10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [New_contact(firstname="", middlename="", lastname="", address="",
                        homephone="", mobilephone="", workphone="",
                        email="", secondary_phone="")] + [
               New_contact(firstname=random_string("name", 10), middlename=random_string("name", 10),
                           lastname=random_string("name", 10), address=random_string("name", 20),
                           homephone=random_string("name", 7), mobilephone=random_string("name", 7),
                           workphone=random_string("name", 7),
                           email=random_string("name", 10), secondary_phone=random_string("name", 7))
               for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))