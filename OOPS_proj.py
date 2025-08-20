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
                          5. Press any other key to exit
                           
                           Select an option: """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_posts()
        elif user_input == '4':
            self.sendmsg()
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

    def my_posts(self):
        if self.loggedin == True:
            txt = input("Write your post: ")
            print(f"Following post is created -> {txt}")
        else:
            print("You need to signin first to post something.")
        print("\n")
        self.menu()
    

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message: ")
            frnd = input("Whom to send the message: ")
            print(f"Message sent to {frnd}: {txt}")
        else:
            print("You need to signin first to send a message.")
        print("\n")
        self.menu()
# user1  = chatbook()