from customer import Customer


class CustomerImpl(Customer):

    def __init__(self, name: str, nid: str, address: str, age: int):
        self.__name = name
        self.__nid = nid
        self.__address = address
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_nid(self):
        return self.__nid

    def set_nid(self, nid):
        self.__nid = nid

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return f"Name: {self.get_name()}, NID: {self.get_nid()},Address: {self.get_address()}, AGE: {self.get_age()}"


customer1 = CustomerImpl("Zuheb", "489669", "Khilgaon", 26)
customer1.set_address("Shahjahanpur")
print(customer1)

