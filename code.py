users = [
    (0, "Bob", "password"),
    (1, "Jake", "Pass123"),
    (2, "Rolf", "Kity231"),
    (3, "Katie", "Jojo2334")
]

username_mapping = {user[1]: user for user in users}

username_input = input("enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Welcome")
else:
    print("Wrong password")