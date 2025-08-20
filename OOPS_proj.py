class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to Chatbook !! how woukd you like to proceed?
                          1. Press 1 to signup
                          2. Press 2 to signin
                          3. Press 3 to write a post
                          4. Press 4 to message a friend
                          5. Press any other key to exit""")
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()
    

    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Setup your password: ")
        self.username = email
        self.password = pwd
        print("Signup successful! You can now Signin.")
        print("\n")
        self.menu()


    def signin(self):
        if self.username == '' and self.password == '':
            print("You need to signup first!")
            self.menu()
        else:
            uname = input("Enter your email/username: ")
            pwd = input("Enter your password: ")
            if uname == self.username and pwd == self.password:
                print("Signin successful!")
                self.loggedin = True
            else:
                print("Invalid credentials, please try again.")
        print("\n")
        self.menu()


obj  = chatbook()