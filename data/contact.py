import random
import string
from model.contact import New_contact

constant = [
    New_contact(firstname="firstname1", middlename="middlename1",
                lastname="lastname1", address="address1",
                homephone="homephone1", mobilephone="mobilephone1",
                workphone="workphone1",
                email="email1", secondary_phone="secondary_phone1"),
    New_contact(firstname="firstname2", middlename="middlename2",
                lastname="lastname2", address="address2",
                homephone="homephone2", mobilephone="mobilephone2",
                workphone="workphone2",
                email="email2", secondary_phone="secondary_phone2"),
]


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
]
