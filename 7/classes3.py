class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_user_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, username, email, privileges):
        super().__init__(username, email)
        self.privileges = Privileges(privileges)

    def __repr__(self):
        return f"Admin\nusername='{self.username}', \nemail='{self.email}', \nprivileges={self.privileges.privileges}"


def main():
    # Create an instance of Admin
    admin_privileges = [
        "can add post",
        "can delete post",
        "can ban user",
        "can view user information"
    ]
    admin_user = Admin("AdminUser", "admin@example.com", admin_privileges)

    # Display user information using __repr__
    print(admin_user)

    # Display admin privileges
    admin_user.privileges.show_privileges()


if __name__ == "__main__":
    main()
