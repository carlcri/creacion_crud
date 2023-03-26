import os

from dotenv import load_dotenv

# Load config from .env file
load_dotenv()
PASSWORD = os.environ["SECRET_KEY"]


def password_required(func):
	def wrapper():
		user_password = input('Digita la constraseña: ')
		if user_password == PASSWORD:
			return func()
		else:
			os.system('echo contraseña incorrecta | lolcat')			
	return wrapper


@password_required
def needs_password():
	os.system('echo accesing private data | cowsay | lolcat')


if __name__ == '__main__':
	needs_password()
	
