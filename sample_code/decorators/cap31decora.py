#  -*- coding: utf-8 -*-



def password_required(func):
	def wrapper():
		user_password = input('Digita la constraseña: ')
		if user_password == PASSWORD:
			return func()
		else:
			print('constraseña incorrecta!')				
	return wrapper


@password_required
def needs_password():
	print('constraseña es correcta')


def upper1(func):
	def wrapper(name):
		print('Hola Bienvenido: esta funcion decoradora solo modifica el nombre')
		name = name.upper()
		return func(name)
#		return func(name).upper()
	return wrapper

@upper1
def print_my_name(name):
	name = 'your name is ' + name
	return name

def upper2(func):
	def wrapper(name):
		print('Hola Bienvenido')
		return func(name).upper()
	return wrapper


@upper2
def print_my_name2(name):
	name = 'your name is ' + name
	return name

def funcion():
	print('Hola')

if __name__ == '__main__':
	this_is_a_name = 'Alvaraco el Paraco'
	print(print_my_name(this_is_a_name))
	print('''
		''')
	print(print_my_name2(this_is_a_name))
	needs_password()

	print('recuerda que si una funccion no retorna nada por defecto retorna None')
	b = funcion()
	print(b)



