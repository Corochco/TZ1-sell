class Contact():
    def __init__(self, full_name, number, email):
        self.full_name = full_name
        self.number = number
        self.email = email
    def email(self):
        return self.email
    def number(self):
        return self.number
    def full_name(self):
        return full_name
    def prnt(self):
        print(self.full_name, self.number, self.email)
        
        