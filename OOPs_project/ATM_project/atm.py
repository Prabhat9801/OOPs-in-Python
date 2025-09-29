class Atm:
# static/class variable - for shared property
    __counter = 1
#magic/special/dunder method
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.sno = Atm.counter
        Atm.__counter += 1
        self.menu()
    @staticmethod
    def get_counter(self):
        return Atm.__counter
    
    @staticmethod
    def set_counter(new_counter):
        if type(new_counter)==int and new_counter>0:
            Atm.__counter = new_counter
            print("Counter updated successfully")
        else:
            print("Counter should be a positive integer")

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin)==str:
            self.__pin = new_pin
            print("Pin updated successfully")
        else:
            print("Pin should be a string")


    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed?
        1. Enter 1 to create a pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposite()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            self.exit()
    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin created successfully")

    def deposite(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter amount to deposit: "))
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Incorrect pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(f"Your balance is {self.__balance}")
        else:
            print("Incorrect pin")

    def exit(self):
        print("Thank you for using the ATM")
          


