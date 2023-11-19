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

@click.group()
def bio():
    pass

@bio.command()
@click.option('--age', type=int, prompt='Your age', help='Your age.')
def age(age):
    """Display age."""
    click.echo(f'You are {age} years old.')

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

@greet.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def salam(name):
    """Simple program that greets NAME with Salam."""
    click.echo(f'Assalamualaikum {name}! Salam sejahtera, apa khabar awak?')

@click.command('all')
def show_all_commands():
    """Print all available commands."""
    ctx = click.get_current_context()
    click.echo("Available Commands:")
    for command in app.cli.commands.values():
        if isinstance(command, click.core.Group):
            click.echo(f" - {command.name}")
            for subcommand in command.commands.values():
                param_info = ", ".join(f"{param.name}: {param.type}" for param in subcommand.params)
                if command.name == 'greet':
                    usage_example = f" --> usage example: flask {command.name} {subcommand.name} --{subcommand.params[0].name} han"
                elif command.name == 'bio':
                    usage_example = f" --> usage example: flask {command.name} {subcommand.name} --{subcommand.params[0].name} 23"
                else:
                    usage_example = f" --> usage example: UNKNOWN"
                click.echo(f"   - {subcommand.name}({param_info}){usage_example}")

        else:
            param_info = ", ".join(f"{param.name}: {param.type}" for param in command.params)
            usage_example = f" --> usage example: flask {command.name}"
            click.echo(f" - {command.name}({param_info}){usage_example}")


app.cli.add_command(greet)
app.cli.add_command(bio)
app.cli.add_command(show_all_commands)

if __name__ == '__main__':
    show_all_commands()
    app.run(debug=True)
