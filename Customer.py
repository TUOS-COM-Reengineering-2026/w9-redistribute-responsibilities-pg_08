class Customer:
    def __init__(self, name: str):
        self._name = name
        self.address = ""
        self.phone_number = ""

    def get_address(self):
        return self.address

    def set_address(self, address: str):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number: str):
        self.phone_number = phone_number

    def set_new_customer(self, address, phone_number):
        self.set_address(address)
        self.set_phone_number(phone_number)

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

