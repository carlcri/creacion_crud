import sys, os
import click


@click.group
def main():
    pass

@main.command
def greeting():
    print('Hola Mundo')


if __name__ == '__main__':
    main()