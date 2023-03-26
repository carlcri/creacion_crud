#!/usr/bin/env python

import click


@click.group
def cli():
    '''
        Basic Operations
    '''
    pass


@cli.command
@click.argument('numbers', nargs=2, type=int, default=(0,0))
def resta(numbers):
    '''
        Resta dos enteros
    '''
    a,b = numbers
    click.echo(click.style(a-b, fg='green'))


@cli.command
@click.argument('numbers', nargs=-1, type=int)
def suma(numbers):
    '''
        Suma varios enteros positivos
    '''
    click.echo(click.style(sum(numbers), fg='red'))



if __name__ == '__main__':
    cli()
