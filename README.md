# sunset_liqour--python


# Overview:

This project is a command-line interface (CLI) application developed for Sunset Liquor Store. It interacts with a database using SQLAlchemy for CRUD (Create, Read, Update, Delete) operations on Customer, Brand, Company, Comment, and Rating entities.

# Features:
Adding Customer Details (customer_input()):

Collects information (name, age, email, address, loyalty points) to create a new customer entry.
Calculates a discount percentage based on loyalty points and displays a discount message.

# Adding Brand Details (brand_input()):

Gathers brand information (name, company ID, category, price, customer ID) to create a new brand entry.

# Adding Company Details (company_input()):

Collects company data (name, location, established year, revenue) to add a new company entry.

# Adding a Comment (add_comment()):

Allows a user to add a comment associated with a specific brand and customer.

# Adding a Rating (add_rating()):

Permits users to add a rating for a particular brand and customer.

# Viewing All Drinks (view_drinks()):

Displays all available drinks (brands) with their respective prices.

# Viewing All Comments (view_all_comments()):

Retrieves and displays all comments stored in the database.

# Viewing All Ratings (view_all_ratings()):

Retrieves and displays all ratings stored in the database.

# Viewing All Companies (view_all_companies()):

Displays all registered companies along with their details.

# Searching Brands (search_brands()):

Searches for brands by name based on user-provided search terms.

# Searching All Entities (search_all()):

Searches for customers, brands, and companies based on a provided search term.

# Main Menu (main_menu()):

Presents a menu with options to execute various functionalities.
How to Run:
Ensure Python and required libraries are installed.
Run the application by executing python your_file_name.py.
Follow the menu prompts to interact with different functionalities.
Libraries Used:
Click: Used for creating a command-line interface.
SQLAlchemy: Handles the ORM (Object-Relational Mapping) for database interactions.


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