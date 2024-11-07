#define the function
def calculate_discount(price, discount_percent):

    #implement the discount if conditions are met
    if discount_percent >= 20:
        discounted_price = price - price * (discount_percent / 100)
        return discounted_price
    else:
        print("For a discount to apply, it should be 20 percent or more")
        return price

#Remove comment from line 13 and 14. Then Comment out line 17 to 23 for part 1 of the solution to apply
#print the new price
#print(calculate_discount(200, 15))


#user input
price = float(input("Please enter the price: "))
discount_percentage = float(input("Please enter the discount: "))

#call the function
final_price = calculate_discount(price, discount_percentage)
print("The final price is:", final_price)
