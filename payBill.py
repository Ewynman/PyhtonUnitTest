import random

def payBill(total_bill, num_guests):
    cost_per_guest = round(total_bill / num_guests, 2)
    leftover = round(total_bill - (cost_per_guest * num_guests), 2)

    guests = ["guest" + str(i+1) for i in range(num_guests)]
    bill_dict = {}
    if leftover > 0:
        extra_index = random.randint(0, num_guests - 1)
    else:
        extra_index = -1
    
    for i in range(num_guests):
        cost = cost_per_guest
        if i == extra_index:
            cost += leftover
        bill_dict[guests[i]] = round(cost, 2)
        if i == extra_index:
            extra_guest = guests[i]

    if leftover > 0:
        return bill_dict, extra_guest
    else:
        return bill_dict, None

total_bill = float(input("Enter the total bill amount including tip: "))
num_guests = int(input("Enter the number of guests: "))

extra_guest = payBill(total_bill, num_guests)
if extra_guest:
    print("The extra amount was assigned to:", extra_guest)
else:
    print("No extra amount was assigned.")