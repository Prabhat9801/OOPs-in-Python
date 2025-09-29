# definition of inheritance - when a class acquires the properties of another class
# parent class - User
# child class - Student
# single level inheritance - when a child class inherits from a single parent class
# multi level inheritance - when a class inherits from a child class
# multiple inheritance - when a class inherits from multiple parent classes
# hierarchical inheritance - when multiple classes inherit from a single parent class
# hybrid inheritance - combination of two or more types of inheritance

class User:
    def login(self):
        print("login")

    def register(self):
        print("Register")

class Student(User):
    def enroll_course(self):
        print("enroll")

    def review_course(self):
        print("review")

stu1 = Student()
stu1.login()
stu1.enroll_course()
stu1.review_course()
stu1.register()