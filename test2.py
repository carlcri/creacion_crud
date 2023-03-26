# Usar:
# py archivo.py
# py archivo.py -n Loro
# py archivo.py --name Loro

import click

@click.command()
#basic option
@click.option('--name', '-n', default = 'Antonia')


def main(name):
    click.echo(f'Your name is {name}')

if __name__ == '__main__':
    main()
