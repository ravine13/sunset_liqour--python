import click
from Main import session, Brand

@click.command()
def view_all_drinks():
    all_drinks = session.query(Brand).all()

    for drink in all_drinks:
        click.echo(click.style(f"Brand: {drink.name}, Price: {drink.price}, Category: {drink.category}", fg='green'))
