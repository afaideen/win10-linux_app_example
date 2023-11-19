# app.py

import sys
sys.path.append('.')
from flask import Flask, render_template
import click
from commands.cmd_greet import hello, hi, salam



def create_app():
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
    def age(age):  # > flask bio age --age 23
        """Display age."""
        click.echo(f'You are {age} years old.')

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
                    if command.name == 'commands':
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

    greet.add_command(hello)
    greet.add_command(hi)
    greet.add_command(salam)

    app.cli.add_command(bio)
    app.cli.add_command(greet)
    app.cli.add_command(show_all_commands)

    show_all_commands()
    return app


app = create_app()

if __name__ == '__main__':

    app.run(debug=True)
