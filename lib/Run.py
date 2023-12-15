import click
from sqlalchemy import and_
from Main import session, Customer, Brand, Rating, Comment
from sqlalchemy import func  

@click.command()
def find_customer():
    customer_name = click.prompt(click.style("Enter the customer name", fg='blue'), type=str)

    customer = session.query(Customer).filter(func.lower(Customer.name) == func.lower(customer_name)).first()

    if customer:
        click.echo(click.style(f"Customer Name: {customer.name}, Email: {customer.email}", fg='green'))

        ratings = session.query(Rating).filter(Rating.customer_id == customer.id).all()
        comments = session.query(Comment).filter(Comment.customer_id == customer.id).all()

        for rating in ratings:
            brand = session.query(Brand).filter(Brand.id == rating.brand_id).first()
            if brand:
                click.echo(f"Chosen Drink: {brand.name}")
                click.echo(f"Rating: {rating.score}")

        for comment in comments:
            click.echo(f"Customer Comment: {comment.text}")
    else:
        click.echo("No matching customer found.")

if __name__ == '__main__':
    find_customer()

