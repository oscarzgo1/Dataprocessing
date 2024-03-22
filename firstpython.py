import random

Monclear = 450
Gucci = 150
Sales_per_month_Store1 = 330

Addidas = 150
Pumma = 140
Nike = 550
Sales_per_month_pumaandnike = 660
List_new = ["Nike", "Pumma", "Addidas"]

class Prestige_Store:
    # Password Generator Function
    @staticmethod
    def generate_password():
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-"
        password = ''.join(random.choice(chars) for i in range(10))
        return password

    # Monthly Sales Calculation for Prestige Store
    @staticmethod
    def montlhy_sales(monclear, gucci, sales):
        monhtly_sales_for_Store1 = (sales * monclear) + (sales * gucci)
        return monhtly_sales_for_Store1

    # Monthly Sales Calculation for ShopLife
    @staticmethod
    def montlhy_sales_of_ShopLife(addias, nike, pumma, sales):
        monthly_sales_shoplife = (sales * nike) + (sales * pumma) + (sales * addias)
        return monthly_sales_shoplife

    # Adding New List of Clothing to ShopLife
    @staticmethod
    def adding_new_list_of_clothing(lst):
        new_list = []
        new_list.extend(lst)
        print("This is are the new Items in the Shoplife Store:", new_list)

    # Checking the Most Expensive and Cheapest Item
    @staticmethod
    def checking_the_most_expensive_and_most_cheapest_item(addidas, nike, pumma):
        cheapest_item = min(addidas, nike, pumma)
        if cheapest_item == addidas:
            print(f"The cheapest item to purchase: Addidas - ${addidas}")
        elif cheapest_item == nike:
            print(f"The cheapest item to purchase: Nike - ${nike}")
        elif cheapest_item == pumma:
            print(f"The cheapest item to purchase: Pumma - ${pumma}")

        expensive_item = max(Gucci, Monclear)
        if expensive_item == Gucci:
            print(f"The most expensive item: Gucci - ${expensive_item}")
        elif expensive_item == Monclear:
            print(f"The most expensive item: Monclear - ${expensive_item}")

    # Total Earnings Calculation
    @staticmethod
    def calculate_total_earnings():
        total_earnings = Prestige_Store.montlhy_sales(Monclear, Gucci, Sales_per_month_Store1) + \
                         Prestige_Store.montlhy_sales_of_ShopLife(Addidas, Nike, Pumma, Sales_per_month_pumaandnike)
        return total_earnings

# Simulating a Credit Card Transaction
def make_payment(total_amount):
    credit_card_balance = 1000  # Assuming initial balance
    if total_amount <= credit_card_balance:
        print("Payment successful!")
        return True
    else:
        print("Insufficient funds! Payment failed.")
        return False

# Main function
if __name__ == "__main__":
    # Calculate total earnings
    total_earnings = Prestige_Store.calculate_total_earnings()
    print("Total earnings of the store:", total_earnings)

    # Add new list of clothing
    Prestige_Store.adding_new_list_of_clothing(List_new)

    # Checking the most expensive and cheapest item
    Prestige_Store.checking_the_most_expensive_and_most_cheapest_item(Addidas, Nike, Pumma)

    # Simulating a purchase
    purchase_amount = 300  # Example purchase amount
    if make_payment(purchase_amount):
        # If payment is successful, unlock ability to purchase
        password = Prestige_Store.generate_password()
        print("Password to unlock ability to purchase:", password)

        # Prompt user to input the password
        user_input = input("Enter the password to unlock the ability to purchase: ")
        if user_input == password:
            print("You have successfully unlocked the ability to purchase.")
            # Additional actions after unlocking ability to purchase can be added here
        else:
            print("Incorrect password. Access denied.")
