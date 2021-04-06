"""
Main program to run delivery service
"""
from delivery import Delivery
from delivery_strategies import PostalDelivery, FedExDelivery, OpayDelivery
from parse_to_currency import format_to_currency
from recipient_info import RecipientInformation

print("Thank you for ordering a book in our store \U0001f600")
print("Input the recipient details, so we ca process your order:")
recipient_name = input("Name: ")
recipient_address = input("Address: ")
recipient_phone_number = input("Phone Number: ")

recipient_information = RecipientInformation(name=recipient_name,
                                             address=recipient_address,
                                             phone_number=recipient_phone_number)

print(f"\nBase delivery charge is {format_to_currency(number=Delivery.minimum_delivery_cost)}")
print(f"""
pick a delivery type below:
  1 Postal Service -> {PostalDelivery.percentage_to_increase_by}% increase
  2 Fedex -> {FedExDelivery.percentage_to_increase_by}% increase
  3 Opay -> {OpayDelivery.percentage_to_increase_by}% increase
""")


def process_delivery(delivery: Delivery):
    delivery.calculate_delivery()
    print(delivery.show)


while True:
    try:
        user_delivery_choice = int(input("Select 1 for postal, 2 for Fedex or 3 for Opay: "))
        if user_delivery_choice == 1:
            postal_delivery = Delivery(recipient_information, PostalDelivery())
            process_delivery(postal_delivery)
            break
        elif user_delivery_choice == 2:
            postal_delivery = Delivery(recipient_information, FedExDelivery())
            process_delivery(postal_delivery)
            break
        elif user_delivery_choice == 3:
            postal_delivery = Delivery(recipient_information, OpayDelivery())
            process_delivery(postal_delivery)
            break
        else:
            print("\nplease try again, so we can process your order\n")
    except ValueError:
        print("\nplease try again, so we can process your order\n")
