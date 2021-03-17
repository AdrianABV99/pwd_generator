from database_manager import store_password, select_app, select_email, select_username, select_all_credentials
from hash_generator import password
class user:
	def __init__(self,name,password,id):
		self.name = name
		self.password = password
		self.id = id

	def new_password(self):
		print("First select an username")
		usr = input()
		print("Name of the app?")
		app = input()
		print("Please input some sample text")
		pt = input()
		print("Also add an email for the app")
		email = input()
		pwd = password(usr, app, pt)
		store_password(pwd, usr, email, app, self.id)
		print(f"New password created, usr:{usr} app:{app} password:{pwd}")
		
	def app_accounts(self):
		print("Enter the name of an app")
		app_name = input()
		accounts = select_app(app_name, self.id)

		if not accounts:
			print(f"no entrys in the database for {app_name}")
		else:
			print(f"All accounts for {app_name}:")
			for i in accounts:
				print(f"Password:{i[0]} --- Username:{i[1]} --- Email:{i[2]}")

	def email_users(self):
		print("Enter an email addres")
		email = input()
		accounts = select_email(email, self.id)
		if not accounts:
			print(f"no entrys in the database for the addres {email}")
		else:
			print(f"All accounts for the addres {email}:")
			for i in accounts:
				print(f"App name:{i[2]} --- Username:{i[1]} --- Password:{i[0]}")

	def username_accounts(self):
		print("Enter an username")
		username = input()
		accounts = select_username(username,self.id)
		if not accounts:
			print(f"no entrys in the database for the addres {username}")
		else:
			print(f"All credentials for the username {username}:")
			for i in accounts:
				print(f"Password:{i[0]} --- App name:{i[1]} --- Emai:{i[2]}")


	def show_all(self):
		accounts = select_all_credentials(self.id)
		if not accounts:
			print("Your account has no info")
		else:
			print("The data from your account consist of:")
			for i in accounts:
				print(f"Username:{i[0]} --- Password:{i[1]} --- App name:{i[2]} --- Password:{i[3]}")
				


#a =user('adi',1234,1)
#a.show_all()	

			