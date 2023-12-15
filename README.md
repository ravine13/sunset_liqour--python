# sunset_liqour--python

# Customers:
•	Get all customers: session.query(Customer).all()
•	Get specific customer by name: session.query(Customer).filter_by(name="John Doe").first()
•	Get customers older than a certain age: session.query(Customer).filter(Customer.age > 21).all()
•	Search customers by name or email: session.query(Customer).filter(or_(Customer.name.contains("search_term"), Customer.email.contains("search_term"))).all()

# Brands:
•	Get all brands: session.query(Brand).all()
•	Get specific brand by ID: session.query(Brand).filter_by(id=1).first()
•	Get brands within a certain price range: session.query(Brand).filter(Brand.price.between(10, 20)).all()
•	Get brands by category: session.query(Brand).filter_by(category="Beer").all()
•	Search brands by name: session.query(Brand).filter(Brand.name.contains("search_term")).all()

# Companies:
•	Get all companies: session.query(Company).all()
•	Get a specific company by name: session.query(Company).filter_by(name="Acme Inc.").first()
•	Get companies established after a certain year: session.query(Company).filter(Company.established_year > 2000).all()
•	Search companies by name or location: session.query(Company).filter(or_(Company.name.contains("search_term"), Company.location.contains("search_term"))).all()

# Comments:
•	Get all comments for a specific brand: session.query(Comment).filter_by(brand_id=1).all()
•	Get all comments by a specific customer: session.query(Comment).filter_by(customer_id=1).all()
•	Search comments for a specific keyword: session.query(Comment).filter(Comment.text.contains("search_term")).all()

# Ratings:
•	Get all ratings for a specific brand: session.query(Rating).filter_by(brand_id=1).all()
•	Get all ratings by a specific customer: session.query(Rating).filter_by(customer_id=1).all()