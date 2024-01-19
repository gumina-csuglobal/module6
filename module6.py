"""
Class holds information about an item that is available for purchase
"""
class ShoppingCart:

    cart_items = []    

    # Default constructor
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name=customer_name
        self.current_date=current_date        

    
    def add_item(self, item_to_purchase):
        pass
        
    def remove_item(self, item_name):

        for idx, item in enumerate(self.cart_items):
            if item.name == item_name:
                del self.cart_items[idx]
                break
        else:
            print("Item not found in cart. Nothing removed.")           
        
    def modify_item(self, item_to_purchase):
        for idx, item in enumerate(self.cart_items):
            if item.name == item_to_purchase.name:                
                break
        else:
            print(" Item not found in cart. Nothing modified.") 

    def get_num_items_in_cart(self):
        pass

    def get_cost_of_cart(self):
        pass

    # Outputs total of objects in cart
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = len(self.cart_items)
        if num_items:
            print(f"Number of Itmes: {num_items}")
        else:
            print("SHOPPING CART IS EMPTY")        

    def print_descriptions(self):
        pass



def print_menu(shopping_cart):
    while True:
        choice = input_choice()
        if choice == "q":
            break
        elif choice == ""


def input_choice():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    return input("Choose an option: ")    


def main():
    print_menu(None)
   

if __name__ == "__main__":
    main()   