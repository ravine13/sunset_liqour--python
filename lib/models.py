import click
from Main import session, Customer, Company, Brand,Rating,Comment


@click.command()
def customer_input():
    name = click.prompt(click.style("Name", fg='blue'), type=str)
    age = click.prompt(click.style("Age", fg='blue'), type=int)
    email = click.prompt(click.style("Email", fg='blue'), type=str)
    address = click.prompt(click.style("Address", fg='blue'), type=str)
    loyalty_points = click.prompt(click.style("Loyalty Points", fg='blue'), type=int)
    brand_id = click.prompt(click.style("Brand ID", fg='blue'), type=int)

    discount_percentage = min(5 + (loyalty_points // 100) * 5, 20)
    discount_message = click.style(f"You get a {discount_percentage}% discount on your purchase!", fg='green')

    if age >= 18:
        click.echo(click.style(f"Hello {name}, your order has been confirmed and it will be delivered to {address}.", fg='green'))
        click.echo(discount_message)
        click.echo(click.style("Thank you for choosing us. Your satisfaction is our priority.", fg='green'))
        
        new_customer = Customer(name=name, age=age, email=email, address=address, loyalty_points=loyalty_points, brand_id=brand_id)
        session.add(new_customer)
        session.commit()
    else:
        click.echo(click.style("Sorry, we cannot process your order.", fg='red'))
        click.echo(click.style("Alcohol is for persons above the age of 18.", fg='red'))


@click.command()
def brand_input():
    brand_name = click.prompt(click.style("Brand Name", fg='blue'), type=str)
    company_id = click.prompt(click.style("Company ID", fg='blue'), type=int)
    category = click.prompt(click.style("Category", fg='blue'), type=str)

    new_brand = Brand(name=brand_name, company_id=company_id, category=category)
    session.add(new_brand)
    session.commit()

    click.echo(click.style(f"Brand '{brand_name}' has been added to the database.", fg='green'))



@click.command()
def company_input():
    company_name = click.prompt(click.style("Company Name", fg='blue'), type=str)
    location = click.prompt(click.style("Location", fg='blue'), type=str)
    established_year = click.prompt(click.style("Established Year", fg='blue'), type=int)
    revenue = click.prompt(click.style("Revenue", fg='blue'), type=float)

   
    new_company = Company(name=company_name, location=location, established_year=established_year, revenue=revenue)
    session.add(new_company)
    session.commit()

    click.echo(click.style(f"Company '{company_name}' has been added to the database.", fg='green'))

@click.command()
def add_comment():
    brand_id = click.prompt(click.style("Brand ID", fg='blue'), type=int)
    comment_text = click.prompt(click.style("Comment", fg='blue'), type=str)
    new_comment = Comment(brand_id=brand_id, text=comment_text)
    session.add(new_comment)
    session.commit()
    click.echo(click.style(f"Your comment has been added.", fg='green'))

@click.command()
def add_rating():
    brand_id = click.prompt(click.style("Brand ID", fg='blue'), type=int)
    rating_score = click.prompt(click.style("Rating (1-5)", fg='blue'), type=int)
    new_rating = Rating(brand_id=brand_id, score=rating_score)
    session.add(new_rating)
    session.commit()
    click.echo(click.style(f"Your rating has been added.", fg='green'))

@click.command()
def view_drinks():
    brands = session.query(Brand).all()
    for brand in brands:
        click.echo(click.style(f"{brand.name} - ${brand.price}", fg='green'))


if __name__ == '__main__':
    commands = {
        "customer_input": customer_input,
        "brand_input": brand_input,
        "company_input": company_input,
        "add_comment": add_comment,
        "add_rating": add_rating,
        "view_drinks": view_drinks
    }
    cli = click.Group(commands=commands)
    cli()

   