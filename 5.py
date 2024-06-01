class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

class UserManager:
    list_of_users = []

    
    def register():
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        username = input("Enter username : ")
        password = int(input("Enter password (integer): "))
        new_user = User(first_name, last_name, username, password)
        UserManager.list_of_users.append(new_user)
        print("Registration successful!")

    
    def login():
        username = input("Enter username:")
        password = int(input("Enter password (integer): "))
        for user in UserManager.list_of_users:
            if user.username == username:
                if user.password == password:
                    print("Login successful!")
                    return
                else:
                    print("Password incorrect.")
                    return
        print("User with this username not found.")

    
    def change_password():
        username = input("Enter username: ")
        old_password = int(input("Enter old password (integer): "))
        new_password = int(input("Enter new password (integer): "))
        for user in UserManager.list_of_users:
            if user.username == username and user.password == old_password:
                user.password = new_password
                print("Password changed successfully!")
                return
        print("Username or old password is incorrect.")

    
    def get_users():
        return UserManager.list_of_users


UserManager.register()
UserManager.login()
UserManager.change_password()
users = UserManager.get_users()
for user in users:
    print(f"User: {user.first_name} {user.last_name}, Username: {user.username}")
