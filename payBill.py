import random

# Define a function named "payBill" that takes in two parameters: "total_bill" and "num_guests"
def payBill(total_bill, num_guests):
    # Calculate the cost per guest, rounding to two decimal places
    cost_per_guest = round(total_bill / num_guests, 2)
    
    # Calculate any leftover amount after dividing the total bill equally among all guests, rounding to two decimal places
    leftover = round(total_bill - (cost_per_guest * num_guests), 2)

    # Create a list of guests based on the number of guests entered by the user
    guests = ["guest" + str(i+1) for i in range(num_guests)]
    
    # Create an empty dictionary to store each guest's bill
    bill_dict = {}
    
    # If there is any leftover amount, randomly choose one guest to add it to
    if leftover > 0:
        extra_index = random.randint(0, num_guests - 1)
    else:
        extra_index = -1
    
    # Iterate over each guest and assign them their bill
    for i in range(num_guests):
        # Each guest's bill is initially set to the cost per guest
        cost = cost_per_guest
        # If this guest is the one that the extra amount should be added to, add it to their bill
        if i == extra_index:
            cost += leftover
        # Store the guest's bill in the dictionary
        bill_dict[guests[i]] = round(cost, 2)
        # If this guest is the one that the extra amount should be added to, remember their name for later
        if i == extra_index:
            extra_guest = guests[i]

    # If there is any leftover amount, return the dictionary of bills and the name of the guest who got the extra amount
    if leftover > 0:
        return bill_dict, extra_guest
    # Otherwise, just return the dictionary of bills
    else:
        return bill_dict, None

# Ask the user for the total bill amount and number of guests
total_bill = float(input("Enter the total bill amount including tip: "))
num_guests = int(input("Enter the number of guests: "))

# Call the "payBill" function with the user's input and store the result in "extra_guest" (which may be None)
bill_dict, extra_guest = payBill(total_bill, num_guests)

# Print out the bill for each guest, formatted with two decimal places
for guest, bill in bill_dict.items():
    print(f"{guest}: ${bill:.2f}")
    
# If there is an extra guest, print their name
if extra_guest:
    print(f"\nThe extra amount was assigned to {extra_guest}.")
# Otherwise, print that no extra guest was assigned
else:
    print("\nNo extra amount was assigned.")