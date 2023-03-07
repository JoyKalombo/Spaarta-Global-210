# Import Table class
# Import unittest or PyTest - Framework assumes unittest but feel free to use either
import unittest

import restaurant

# Write your tests here (assumes unittest is being used. Can use PyTest if you prefer)
class UnitTests():
    

    def test_order(self):
        self.assertEqual(order({"item": "broccoli", "price": 4.55, "quantity": 2},5.00, 14.10))
        self.assertEqual(order({"item": "broccoli", "price": 4.55}, 2.00, 6.55))

    def test_order_no_quantity(self):
        self.assertEqual()


    def test_remove(self):
        self.assertEqual(remove({"item": "broccoli", "price": 4.55, "quantity": 2},50.00, 40.90))
        self.assertEqual(remove({"item": "broccoli", "price": 4.55}, 50.00, 45.45))

    def test_remove_no_item(self):


    def test_get_subtotal(self):


    def test_get_total(self):


    def test_split_bill(self):




if __name__ == "__main__":
    unittest.main()