import unittest

from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
    def positiveprice(self):
        # Check that the discount price is more than 0
        self.assertEqual(discount_cost > 0)

    def allfieldsinteger(self):
    	with self.assertRaises(ValueError):
    		int(item_cost) = True 
    		## and int(relative_discount) = True and int(absolute_discount) = True

if __name__ == "__main__":
    unittest.main()