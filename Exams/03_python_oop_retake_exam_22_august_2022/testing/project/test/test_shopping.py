from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Teo", 1000)

    def test_init(self):
        self.assertEqual(self.cart.shop_name, "Teo")
        self.assertEqual(self.cart.budget, 1000)
        self.assertEqual(self.cart.products, {})

    def test_shop_name_invalid(self):
        with self.assertRaises(ValueError) as error:
            self.cart.shop_name = "teo"
        self.assertEqual(str(error.exception), "Shop must contain only letters and must start with capital letter!")
        with self.assertRaises(ValueError) as error:
            self.cart.shop_name = "Teo93"
        self.assertEqual(str(error.exception), "Shop must contain only letters and must start with capital letter!")
        with self.assertRaises(ValueError) as error:
            self.cart.shop_name = "teo93"
        self.assertEqual(str(error.exception), "Shop must contain only letters and must start with capital letter!")
        with self.assertRaises(ValueError) as error:
            self.cart.shop_name = "123"
        self.assertEqual(str(error.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_invalid(self):
        with self.assertRaises(ValueError) as error:
            self.cart.add_to_cart("Apple", 100)
        self.assertEqual(str(error.exception), "Product Apple cost too much!")
        with self.assertRaises(ValueError) as error:
            self.cart.add_to_cart("Apple", 200)
        self.assertEqual(str(error.exception), "Product Apple cost too much!")

    def test_add_to_cart_valid(self):
        self.assertEqual(self.cart.add_to_cart("Apple", 99), "Apple product was successfully added to the cart!")
        self.assertEqual(self.cart.products, {"Apple": 99})
        self.cart.add_to_cart("Orange", 10)
        self.assertEqual(self.cart.products, {"Apple": 99, "Orange": 10})

    def test_remove_from_cart_invalid(self):
        with self.assertRaises(ValueError) as error:
            self.cart.remove_from_cart("Apple")
        self.assertEqual(str(error.exception), "No product with name Apple in the cart!")

    def test_remove_from_cart_valid(self):
        self.cart.add_to_cart("Apple", 99)
        self.cart.add_to_cart("Orange", 20)
        self.assertEqual(self.cart.remove_from_cart("Apple"), "Product Apple was successfully removed from the cart!"),
        self.assertEqual(self.cart.products, {"Orange": 20})

    def test_add(self):
        other_cart = ShoppingCart("Bakery", 1000)
        other_cart.add_to_cart("Orange", 10)
        self.cart.add_to_cart("Apple", 10)
        new_cart = self.cart + other_cart
        self.assertEqual(new_cart.shop_name, "TeoBakery")
        self.assertEqual(new_cart.budget, 2000)
        self.assertEqual(new_cart.products, {"Apple": 10, "Orange": 10})

    def test_buy_products_equal(self):
        self.cart.budget = 10
        self.cart.add_to_cart("Apple", 10)
        self.assertEqual(self.cart.buy_products(), f'Products were successfully bought! Total cost: 10.00lv.')

    def test_buy_products(self):
        self.cart.add_to_cart("Apple", 10)
        self.assertEqual(self.cart.buy_products(), f'Products were successfully bought! Total cost: 10.00lv.')

    def test_buy_products_not_enough_money(self):
        self.cart.budget = 0
        self.cart.add_to_cart("Apple", 10)
        with self.assertRaises(ValueError) as error:
            self.cart.buy_products()
        self.assertEqual(str(error.exception), "Not enough money to buy the products! Over budget with 10.00lv!")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/3591#2
