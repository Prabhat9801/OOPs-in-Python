# intiate the class

class employee:
    #Special function / Method . magic method / dunder method
    def __init__(self):
        print("Started executing at attributes/data")
        self.id = 173
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data are initialized")

    def travel(self, destination):
        print("this travel method is called manually")
        print(f"Employee is travelling to {destination}")


    # creating an instance or object
sam = employee()
# calling the method

sam.travel("Bangalore")
# orinting the attributes
print(sam.id)
print(sam.salary)   
print(sam.designation)  

