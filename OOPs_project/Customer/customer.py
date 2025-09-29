class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)

class Address:
    def __init__(self, city, pin_code, State):
        self.city = city
        self.pin_code = pin_code
        self.State = State

    def change_address(self, new_city, new_pin_code, new_state):
        self.city = new_city
        self.pin_code = new_pin_code
        self.State = new_state

add = Address("Bangalore", 560037, "Karnataka")

cust = Customer("Prabhat", "Male", add)

cust.edit_profile("Prabhat Kumar", "Mumbai", 400001, "Maharashtra")
cust.edit_profile("PK", "Chennai", 600001, "Tamil Nadu")

print(cust.name)

print(cust.address.city)
print(cust.address.pin_code)
print(cust.address.State)