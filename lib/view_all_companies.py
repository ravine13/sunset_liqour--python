import click
from Main import session, Company

@click.command()
def view_all_companies():
    all_companies = session.query(Company).all()

    for company in all_companies:
        click.echo(click.style(f"Company Name: {company.name}, Location: {company.location}, Established Year: {company.established_year}, Revenue: {company.revenue}", fg='green'))
