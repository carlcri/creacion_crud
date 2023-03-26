#!/usr/bin/env python

import sys, os
import click


@click.group
def main():
    pass


@main.command
def create_tables():
    print('Tablas Creadas exitosamente')


@main.command
@click.argument('username')
@click.option('--age', '-a', default=30)
@click.option('--active', '-e', is_flag=True)
def create_user(username, age, active):
    print('Usuario: {} , creado exitosamente'.format(username))
    print('Edad del usuario: {}'.format(age))

    if(active):
        print('estado: activo')


if __name__ == '__main__':
    main()
