import unittest

import taxes

class ProductTestCase(unittest.TestCase):
    def test_parse_book(self):
        product = taxes.parse("1 book at 12.49")
        self.assertEqual(product.quantity, 1)
        self.assertEqual(product.type, "book")
        self.assertEqual(product.name, "book")
        self.assertEqual(product.cost, 12.49)
        self.assertFalse(product.imported)

    def test_chocolate(self):
        product = taxes.parse("1 imported box of chocolates at 10.00")
        self.assertEqual(product.quantity, 1)
        self.assertEqual(product.type, "food")
        self.assertEqual(product.name, "box of chocolates")
        self.assertEqual(product.cost, 10.0)
        self.assertTrue(product.imported)


class DisplayTestCase(unittest.TestCase):
    def test_correct_output(self):
        input = """1 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85"""
        output = """1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83
"""
        products = taxes.read_products(input)
        self.assertEqual(taxes.to_str(products), output)
