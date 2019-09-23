print()
goods = dict(apple=[24, 30], orange=[5, 40],
             pineapple=[25, 9], papaya=[20, 13])
for fruit, price in goods.items():
    print(f"\t\t\t\t\t\t{fruit} --> Price = {price[0]}, Quantity = {price[1]}")
print()
total = 0
question = "yes"
while question == 'yes':
    fruit_name = input("Enter name of the fruit: ").lower()
    quantity = int(input("Enter quantity: "))
    if 0 < quantity <= goods[fruit_name][1]:
        goods[fruit_name][1] -= quantity
        final_price = goods[fruit_name][0] * quantity
        total += final_price
        question = input("\nWant to continue? YES or NO: ").lower()
        print()
        if question == 'yes':
            for fruit, price in goods.items():
                print(f"{fruit} --> Price = {price[0]}, Quantity = {price[1]}")
        print()
    elif quantity < 0:
        print("\nInvalid Quantity...You Enter Negative Value\n")
        question = input("Want to continue? YES or NO: ").lower()
        print()
    else:
        print("\nSorry....Available quantity is less than your required quantity\n")
        enter = input("Press Enter button to view the list\n")
        for fruit, price in goods.items():
            print(f"{fruit} --> Price = {price[0]}, Quantity = {price[1]}")
        question = input("\nWant to continue? YES or NO: ").lower()
print(f"Total price = {total}")

print("~~ Thank You ~~")
print()
print()
print()
