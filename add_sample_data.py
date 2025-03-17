import os
import django
import pandas as pd

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cashback.settings')
django.setup()

from django.contrib.auth.models import User
from user_login.models import Customer, Item, Department, Cart, Buy

def add_sample_data():
    """
    Add sample data to ensure the recommendation system works.
    This includes:
    1. Creating sample items with appealing names if they don't exist
    2. Updating items in check.csv to have proper names
    """
    print("=== Adding Sample Data ===\n")
    
    # Define appealing product names for each item ID
    appealing_names = {
        1: "Organic Banana Bunch",
        2: "Fresh Strawberries (16 oz)",
        3: "Organic Baby Spinach",
        4: "Ripe Avocado",
        5: "Organic Whole Milk",
        6: "Greek Yogurt (Plain)",
        7: "Aged Cheddar Cheese",
        8: "Artisan Sourdough Bread",
        9: "Whole Grain Bagels (6 pack)",
        10: "Premium Smartphone",
        11: "Ultrabook Laptop",
        12: "Cotton T-shirt (Black)",
        13: "Designer Jeans",
        14: "Modern Sectional Sofa",
        15: "Memory Foam Mattress",
        16: "Moisturizing Shampoo",
        17: "Luxury Makeup Set",
        18: "Daily Multivitamins",
        19: "Extra Strength Pain Reliever",
        20: "Collectible Action Figure",
        21: "Strategy Board Game",
        22: "Professional Basketball",
        23: "Carbon Fiber Tennis Racket"
    }
    
    # Check if check.csv exists
    check_csv_path = os.path.join('data', 'check.csv')
    if not os.path.exists(check_csv_path):
        print("Error: check.csv does not exist")
        return
    
    # Load check.csv
    df = pd.read_csv(check_csv_path)
    print(f"Loaded {len(df)} item relationships from check.csv")
    
    # Get all item IDs from check.csv
    item_ids = set()
    for _, row in df.iterrows():
        if not pd.isna(row['item1']) and row['item1'] != '':
            item_ids.add(int(row['item1']))
        if not pd.isna(row['item2']) and row['item2'] != '':
            item_ids.add(int(row['item2']))
    
    print(f"Found {len(item_ids)} unique item IDs in check.csv")
    
    # Check which items exist in the database
    existing_items = Item.objects.filter(id__in=item_ids)
    existing_item_ids = set(existing_items.values_list('id', flat=True))
    missing_item_ids = item_ids - existing_item_ids
    
    print(f"Found {len(existing_items)} existing items in the database")
    print(f"Missing {len(missing_item_ids)} items")
    
    # Create sample department if it doesn't exist
    dept_name = "Grocery"
    sample_dept, created = Department.objects.get_or_create(id=1, defaults={'name': dept_name})
    if created:
        print(f"Created department: {sample_dept.name}")
    else:
        print(f"Using existing department: {sample_dept.name}")
    
    # Create missing items
    created_items = []
    for item_id in missing_item_ids:
        # Use appealing name if available, otherwise generate one
        if item_id in appealing_names:
            item_name = appealing_names[item_id]
        else:
            category_names = ["Gourmet", "Premium", "Organic", "Artisan", "Handcrafted", "Luxury", "Fresh", "Natural"]
            product_types = ["Food", "Snack", "Beverage", "Accessory", "Tool", "Gadget", "Clothing", "Home Decor"]
            
            # Generate a more appealing name based on item_id
            category = category_names[item_id % len(category_names)]
            product = product_types[(item_id * 3) % len(product_types)]
            item_name = f"{category} {product} #{item_id}"
        
        item = Item.objects.create(id=item_id, name=item_name, dept=sample_dept)
        created_items.append(item)
    
    print(f"Created {len(created_items)} new items")
    
    # Update existing items with empty names
    updated_items = []
    for item in existing_items:
        if not item.name or item.name.startswith("Sample Item"):
            # Use appealing name if available, otherwise generate one
            if item.id in appealing_names:
                item.name = appealing_names[item.id]
            else:
                category_names = ["Gourmet", "Premium", "Organic", "Artisan", "Handcrafted", "Luxury", "Fresh", "Natural"]
                product_types = ["Food", "Snack", "Beverage", "Accessory", "Tool", "Gadget", "Clothing", "Home Decor"]
                
                # Generate a more appealing name based on item_id
                category = category_names[item.id % len(category_names)]
                product = product_types[(item.id * 3) % len(product_types)]
                item.name = f"{category} {product} #{item.id}"
            
            item.save()
            updated_items.append(item)
    
    print(f"Updated {len(updated_items)} existing items with appealing names")
    
    # Print summary of all items in check.csv
    print("\n=== Items in check.csv ===")
    for item_id in sorted(item_ids):
        try:
            item = Item.objects.get(id=item_id)
            print(f"Item {item_id}: {item.name}")
        except Item.DoesNotExist:
            print(f"Item {item_id}: Not found in database")
    
    print("\n=== Sample Data Added Successfully ===")
    print("You should now be able to see recommendations with appealing product names when you add these items to your cart.")

if __name__ == "__main__":
    add_sample_data() 