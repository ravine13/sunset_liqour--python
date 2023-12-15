import click
from Main import session, Comment

@click.command()
def view_all_comments():
    all_comments = session.query(Comment).all()

    for comment in all_comments:
        click.echo(click.style(f"Customer ID: {comment.customer_id}, Brand ID: {comment.brand_id}, Comment: {comment.text}", fg='green'))