class Parent:
    def __init__(self):
        self.__num = 100  # private variable


    def show(self):
        print("Parent class show method")
        print("Parent class private variable:", self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 200  # private variable

    def show(self):
        print("Child class show method")
        print("Child class private variable:", self.__var)

dad = Parent()
dad.show()
son = Child()
son.show()  # calls the show method of the Child class