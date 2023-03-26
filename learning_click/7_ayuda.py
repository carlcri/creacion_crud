#!/usr/bin/env python

import click


@click.group()
def cli():
    '''
        Manages database
    '''    
    pass


@cli.command()
@click.argument('db_name', default='zip_codes')
@click.option('--permanent', '-p', is_flag=True)
def drop_db(db_name, permanent):
    '''
        Warning: Deletes database
    '''
    if(permanent):
        click.echo(f'database: {db_name} being dropped')
    else:
        click.echo(f'database: {db_name} still in unit')   

    click.echo(click.style(db_name, fg='green'))   
    click.echo(click.style('Bold Text', bold=True)) 
    click.echo(click.style('backgrond color', bg='blue'))

    


@cli.command()
def create_db():
    '''
        Creates Database
    '''

    click.echo('Creates database')

if __name__ == '__main__':
    cli()



    
