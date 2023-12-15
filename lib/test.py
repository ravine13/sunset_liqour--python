from models import session,Rating,Brand,Comment,Company,Customer
import click
from sqlalchemy import or_

# hello = session.query(Rating).filter_by(brand_id=1).all()

# for rating in hello:
#         brand = session.query(Brand).filter(Brand.id == rating.brand_id).first()
#         if brand:
#             print(f"Chosen Drink: {brand.name}")
#             print(f"Rating: {rating.score}")


specific_brand_comments = session.query(Comment).filter_by(brand_id=1).all()

# print(specific_brand_comments)

specific_customer_comments = session.query(Comment).filter_by(customer_id=1).all()

# print(specific_customer_comments)

all_companies = session.query(Company).all()
# print(all_companies)

specific_company = session.query(Company).filter_by(name="EABL").first()

# print(specific_company)

companies_after_2000 = session.query(Company).filter(Company.established_year > 2000).all()

# print(companies_after_2000)

search_term = "your_search_term"
searched_companies = session.query(Company).filter(or_(Company.name.contains(search_term), Company.location.contains(search_term))).all()

# print(searched_companies)

all_brands = session.query(Brand).all()
# print(all_brands)

specific_brand = session.query(Brand).filter_by(id=1).first()

# print(specific_brand)

brands_in_price_range = session.query(Brand).filter(Brand.price.between(200, 1000)).all()

# print(brands_in_price_range)

brands_by_category = session.query(Brand).filter_by(category="Gin").all()

# print(brands_by_category)

search_term = "your_search_term"
searched_brands = session.query(Brand).filter(Brand.name.contains(search_term)).all()

# print(searched_brands)

all_customers = session.query(Customer).all()

print(all_customers)

specific_customer = session.query(Customer).filter_by(name="Njeri").first()

# print(specific_customer)

customers_older_than_21 = session.query(Customer).filter(Customer.age > 21).all()

# print(customers_older_than_21)

search_term = "your_search_term"
searched_customers = session.query(Customer).filter(or_(Customer.name.contains(search_term), Customer.email.contains(search_term))).all()

# print(searched_customers)


