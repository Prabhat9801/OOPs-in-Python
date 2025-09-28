class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
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
        self.pin = input("Enter your pin: ")
        print("Pin created successfully")

    def deposite(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Incorrect pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Incorrect pin")

    def exit(self):
        print("Thank you for using the ATM")
          


