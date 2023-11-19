import click



@click.command()
@click.option('--name', prompt='Your name', help='The person to commands.')
def hello(name):    # > flask commands hello --name han
    """Simple program that greets NAME."""
    click.echo(f'Hello {name.capitalize()}, how can I help you?')

@click.command()
@click.option('--name', prompt='Your name', help='The person to commands.')
def hi(name):   # > flask commands hi --name han
    """Simple program that greets NAME."""
    click.echo(f'Hi {name.capitalize()}, how are you getting on?')

@click.command()
@click.option('--name', prompt='Your name', help='The person to commands.')
def salam(name):
    """Simple program that greets NAME with Salam."""
    click.echo(f'Assalamualaikum {name}! Salam sejahtera, apa khabar awak?')