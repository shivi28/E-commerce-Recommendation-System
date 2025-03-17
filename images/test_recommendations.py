import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cashback.settings')
django.setup()

from django.contrib.auth.models import User
from user_login.models import Customer, Item, Cart

def add_test_items_to_cart(username):
    """
    Add test items to a user's cart for testing the recommendation system.
    
    Args:
        username: The username of the user to add items to their cart
    """
    try:
        # Get the user
        user = User.objects.get(username=username)
        print(f"Found user: {user.username}")
        
        # Check if the user has a customer profile
        try:
            customer = user.customer
            print(f"Found customer profile for {username}")
        except Customer.DoesNotExist:
            print(f"Error: No customer profile for {username}")
            return
        
        # Clear existing cart items
        Cart.objects.filter(user=customer).delete()
        print("Cleared existing cart items")
        
        # Define test item IDs to add to cart
        test_item_ids = [1, 2, 3]  # These items have relationships in check.csv
        
        # Add test items to cart
        for item_id in test_item_ids:
            try:
                item = Item.objects.get(id=item_id)
                cart_item = Cart(user=customer, item=item)
                cart_item.save()
                print(f"Added item {item_id} ({item.name}) to cart")
            except Item.DoesNotExist:
                print(f"Item with ID {item_id} does not exist")
            except Exception as e:
                print(f"Error adding item {item_id} to cart: {e}")
        
        # Count items in cart
        cart_count = Cart.objects.filter(user=customer).count()
        print(f"\nUser now has {cart_count} items in their cart")
        print("Refresh the home page to see recommendations")
        
    except User.DoesNotExist:
        print(f"User '{username}' not found")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Enter your username: ")
    
    add_test_items_to_cart(username) 