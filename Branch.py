from Staff import Staff


class Branch:

    def __init__(self, location):
        self._location = location
        self._staff = []
        self.opening_time = ""

    def get_opening_time(self):
        return self.opening_time

    def set_opening_time(self, time:str):
        self.opening_time = time

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff

    def add_staff_member(self, staff: Staff):
        self.get_staff().append(staff)
    
    def remove_staff_member(self, staff: Staff):
        self.get_staff().remove(staff)
