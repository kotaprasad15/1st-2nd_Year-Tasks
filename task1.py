import csv
import bcrypt

csv_file = 'login.csv'
fieldnames = ['Username', 'Email', 'Password', 'salt']

def user_register():
    user_id = input("Enter username: ")
    user_mailid = input("Enter your mail id: ")
    user_password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    return user_mailid, user_id, user_password, confirm_password

def user_login():
    user_id = input("Enter your user id: ")
    password = input("Enter password: ")
    return user_id, password

while True:
    with open(csv_file, 'r') as db:
        db_reader = csv.DictReader(db)
        user_data = {row['Username']: {'Email': row['Email'], 'Password': row['Password'], 'salt': row['salt']} for row in db_reader}

        lr = input("Login - [Type L]\nRegister - [Type R]\nExit - [Type E]")

        if lr.lower() == 'l':
            user_id, user_password = user_login()

            if user_id in user_data:
                stored_password_hash = user_data[user_id]['Password']
                stored_salt = user_data[user_id].get('salt')

                if stored_salt is not None and bcrypt.checkpw(user_password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                    print("You logged in successfully")
                else:
                    print("Please check your credentials.")
            else:
                print("Username not found")

        elif lr.lower() == 'r':
           user_mailid, user_id, user_password, confirm_password = user_register()
           with open(csv_file, 'a', newline='') as db:
               header_writer = csv.DictWriter(db, fieldnames)

               if db.tell() == 0:
                    header_writer.writeheader()

               if user_id in user_data:
                    print("Username is already taken")
               elif user_password == confirm_password:
                    salt = bcrypt.gensalt(rounds=16)
                    hashed_password = bcrypt.hashpw(confirm_password.encode('utf-8'), salt)
                    csv_writer = csv.DictWriter(db, fieldnames)
                    csv_writer.writerow({'Username': user_id, 'Email': user_mailid, 'Password': hashed_password.decode('utf-8'), 'salt': salt.decode('utf-8')})
                    print("Successfully registered")
               else:
                    print("Passwords don't match. Try again")

        elif lr.lower() == 'e':
            break