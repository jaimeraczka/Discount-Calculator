def calculate_discount(item_cost,relative_discount,absolute_discount):
	""" Calculate discounted cost of an item """
	discount_cost = item_cost - (item_cost * (relative_discount/100)) - absolute_discount

	return discount_cost








def main():
    discount_cost = calculate_discount(100,10,30)
    print discount_cost

if __name__ == "__main__":
    main()