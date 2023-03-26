#!/usr/bin/env python

import os, click
from dotenv import load_dotenv

# Load config from .env file
load_dotenv()
PASSWORD = os.environ["SECRET_KEY"]

@click.group
def main():
	pass


@main.command
@click.argument('username')
@click.option('--password', '-p', prompt='Enter Password', hide_input=True)
def login(username, password):
	print(username)

	if password == PASSWORD:
		os.system('echo accesing private data | cowsay | lolcat')
	else:
		os.system('echo contraseña incorrecta | lolcat')


if __name__ == '__main__':
	main()
	
