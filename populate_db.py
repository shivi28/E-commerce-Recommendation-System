import os
import django
import random
import string

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cashback.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Category, Offer, SiteData
from user_login.models import Company, Customer, Department, Item

def create_categories():
    """Create sample categories"""
    categories = [
        {'name': 'Electronics', 'description': 'Electronic devices and gadgets'},
        {'name': 'Fashion', 'description': 'Clothing, shoes, and accessories'},
        {'name': 'Home', 'description': 'Home decor and furniture'},
        {'name': 'Beauty', 'description': 'Beauty and personal care products'},
        {'name': 'Sports', 'description': 'Sports equipment and accessories'},
        {'name': 'Books', 'description': 'Books, e-books, and audiobooks'},
        {'name': 'Toys', 'description': 'Toys and games for all ages'},
        {'name': 'Food', 'description': 'Food and grocery items'},
    ]
    
    created_categories = []
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data['name'],
            defaults={
                'description': category_data['description'],
                'alt_tag': category_data['name'],
                'metatags': category_data['name']
            }
        )
        created_categories.append(category)
        print(f"Category {'created' if created else 'already exists'}: {category.name}")
    
    return created_categories

def create_companies():
    """Create sample companies"""
    companies = [
        {'name': 'Amazon', 'description': 'Online shopping platform'},
        {'name': 'Flipkart', 'description': 'E-commerce company'},
        {'name': 'Myntra', 'description': 'Fashion e-commerce platform'},
        {'name': 'Snapdeal', 'description': 'Online marketplace'},
        {'name': 'Shopify', 'description': 'E-commerce platform'},
        {'name': 'eBay', 'description': 'Online auction and shopping website'},
        {'name': 'Walmart', 'description': 'Multinational retail corporation'},
        {'name': 'Target', 'description': 'Retail corporation'},
    ]
    
    created_companies = []
    for company_data in companies:
        company, created = Company.objects.get_or_create(
            name=company_data['name'],
            defaults={
                'description': company_data['description'],
                'page_description': company_data['description'],
                'alt_tag': company_data['name'],
                'metatags': company_data['name']
            }
        )
        created_companies.append(company)
        print(f"Company {'created' if created else 'already exists'}: {company.name}")
    
    return created_companies

def create_offers(categories, companies):
    """Create sample offers"""
    offers_data = [
        {'description': '20% off on Electronics', 'url': 'https://www.amazon.com', 'hot': 1, 'expired': 0},
        {'description': '30% off on Fashion', 'url': 'https://www.myntra.com', 'hot': 1, 'expired': 0},
        {'description': '15% off on Home Decor', 'url': 'https://www.snapdeal.com', 'hot': 1, 'expired': 0},
        {'description': 'Buy 1 Get 1 Free on Beauty Products', 'url': 'https://www.flipkart.com', 'hot': 1, 'expired': 0},
        {'description': '50% off on Sports Equipment', 'url': 'https://www.ebay.com', 'hot': 1, 'expired': 0},
        {'description': '25% off on Books', 'url': 'https://www.amazon.com', 'hot': 1, 'expired': 0},
        {'description': '40% off on Toys', 'url': 'https://www.walmart.com', 'hot': 1, 'expired': 0},
        {'description': '10% off on Food Items', 'url': 'https://www.target.com', 'hot': 1, 'expired': 0},
    ]
    
    created_offers = []
    for i, offer_data in enumerate(offers_data):
        company = companies[i % len(companies)]
        category = categories[i % len(categories)]
        
        offer, created = Offer.objects.get_or_create(
            description=offer_data['description'],
            company=company,
            category=category,
            defaults={
                'url': offer_data['url'],
                'hot': offer_data['hot'],
                'expired': offer_data['expired'],
                'coupon_code': ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            }
        )
        created_offers.append(offer)
        print(f"Offer {'created' if created else 'already exists'}: {offer.description}")
    
    return created_offers

def create_site_data():
    """Create site data"""
    site_data, created = SiteData.objects.get_or_create(
        id=1,
        defaults={
            'alt_tag1': 'Home Banner 1',
            'alt_tag2': 'Home Banner 2',
            'alt_tag3': 'Home Banner 3',
            'alt_tag4': 'Home Banner 4',
        }
    )
    print(f"SiteData {'created' if created else 'already exists'}")
    return site_data

def create_departments():
    """Create departments from CSV data"""
    departments = Department.objects.all()
    if departments.count() == 0:
        from main.views import fillDept
        from django.http import HttpRequest
        request = HttpRequest()
        fillDept(request)
        print("Departments created from CSV data")
    else:
        print(f"Departments already exist: {departments.count()} departments")
    return Department.objects.all()

def create_items(departments):
    """Create items from CSV data"""
    items = Item.objects.all()
    if items.count() == 0:
        from main.views import fillItem, addItemName
        from django.http import HttpRequest
        request = HttpRequest()
        fillItem(request)
        addItemName(request)
        print("Items created from CSV data")
    else:
        print(f"Items already exist: {items.count()} items")
    return Item.objects.all()

if __name__ == '__main__':
    print("Starting database population...")
    
    # Create categories
    categories = create_categories()
    
    # Create companies
    companies = create_companies()
    
    # Create offers
    offers = create_offers(categories, companies)
    
    # Create site data
    site_data = create_site_data()
    
    # Create departments
    departments = create_departments()
    
    # Create items
    items = create_items(departments)
    
    print("Database population completed!") 