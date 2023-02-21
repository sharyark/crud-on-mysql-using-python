from dbhelper import DBhelper

class Portal:
    def __init__(self) -> None:
        # connect to db
        self.db = DBhelper()
        self.menu()
# main function
    def menu(self):
        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave""")

        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else:
            print('you leaved')
    # registration function
    def register(self):
        name = input('Enter your name:')
        email = input('Enter your email:')
        password = input('Enter your password:')
        response = self.db.register(name,email,password)
        if(response):
            print("register successfully")
        else:
            print('registration failed ...')
        self.menu()
# login function
    def login(self):
        email = input("Enter email:")
        password = input("Enter pwd:")
        response = self.db.search(email,password)
        if(len(response) == 0):
            print('No such acount is available..')
        else:
            print(response)


obj = Portal()
obj.menu()