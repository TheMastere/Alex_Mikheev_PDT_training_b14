import pymysql.cursors
from model.contact import New_contact
from model.group import Group

class DbFixture:

    def __init__(self, host, port, name, user, password):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, port=port, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, middlename, company, address, home, mobile, work, email from addressbook")
            for row in cursor:
                (id, firstname, lastname, middlename, company, address, home, mobile, work, email) = row
                contact_list.append(New_contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename, company=company,
                                  address=address, homephone=home, mobilephone=mobile, workphone=work, email=email))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()