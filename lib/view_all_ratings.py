import click
from Main import session, Rating

@click.command()
def view_all_ratings():
    all_ratings = session.query(Rating).all()

    for rating in all_ratings:
        click.echo(click.style(f"Customer ID: {rating.customer_id}, Brand ID: {rating.brand_id}, Rating: {rating.score}", fg='green'))
