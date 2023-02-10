from main import Cart, Item
import unittest


class Cart_test(unittest.TestCase):
    def test_add(self):
        test_cart = Cart()
        test_cart.add('Avocado', 5, 3.28)
        
    def test_delete(self):
        test_cart = Cart()
        test_cart.add('Avocado', 5, 3.28)
        test_cart.delete('Avocado')
        
    def test_show(self):
        test_cart = Item('Avocado', 5, 3.28)
        self.assertEqual(test_cart.name, 'Avocado')
        self.assertEqual(test_cart.quantity, 5)
        self.assertEqual(test_cart.price, 3.28)
            
            
        

        
unittest.main()
