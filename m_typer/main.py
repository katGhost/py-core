import typer
from typing import Optional

app = typer.Typer()


def hello(name: Optional[str] = None):
    names = ['Kat', 'Richard', 'Dinesh']

    if name in [n for n in names]:
        typer.echo(f"Hello, {name}")
    else:
        typer.echo("Hello, World")





if __name__ == "__main__":
    app()
