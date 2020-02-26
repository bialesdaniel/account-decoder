import click
import random

RANDOM_ADJUSTMENT = 3

@click.group()
def cli():
    pass

@cli.command()
@click.option('-a','--account-number',prompt='Enter the encoded account number')
@click.option('-d','--delimeter', default=' ')
def decode(account_number, delimeter):
    private_key = click.prompt('Enter the private key pair (i.e. 7,10)', hide_input=True)
    private_key = list(map(lambda x: int(x),private_key.split(',')))
    numbers = account_number.split(delimeter)
    real_numbers = map(lambda number: str(mod_decode(private_key[0],private_key[1],int(number))),numbers)
    click.echo("Account Number: "+ "".join(real_numbers))

def mod_decode(public,private,num):
    key = private * 10 ** RANDOM_ADJUSTMENT
    return (num+public) % key

if __name__ == '__main__':
    cli()
