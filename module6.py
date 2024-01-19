"""
Class holds information about an item that is available for purchase
"""
class ShoppingCart:

    cart_items = []    

    # Default constructor
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name=customer_name
        self.current_date=current_date        

    
    def add_item(self):
        pass
    def remove_item(self):
        pass

    def modify_item(self):
        pass

    def get_num_items_in_cart(self):
        pass

    def get_cost_of_cart(self):
        pass

    def print_total(self):
        pass

    def print_descriptions(self):
        pass



def print_menu(shopping_cart):
    while True:
        choice = input_choice()
        if choice == "q":
            break


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