# app.py
from flask import Flask, render_template
import click

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@click.group()
def greet():
    pass

@greet.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):    # > flask greet hello --name han
    """Simple program that greets NAME."""
    click.echo(f'Hello {name.capitalize()}, how can I help you?')

@greet.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hi(name):   # > flask greet hi --name han
    """Simple program that greets NAME."""
    click.echo(f'Hi {name.capitalize()}, how are you getting on?')

@click.command('all')
def show_all_commands():
    """Print all available commands."""
    ctx = click.get_current_context()
    click.echo("Available Commands:")
    for command in app.cli.commands.values():
        if isinstance(command, click.core.Group):
            click.echo(f" - {command.name}")
            for subcommand in command.commands.values():
                params = ", ".join(f"{param.name}: {param.type}" for param in subcommand.params)
                click.echo(f"   - {subcommand.name}({params})")
        else:
            click.echo(f" - {command.name}")

app.cli.add_command(greet)
app.cli.add_command(show_all_commands)

if __name__ == '__main__':
    show_all_commands()
    app.run(debug=True)
