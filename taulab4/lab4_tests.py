import unittest
from lab4 import sum, product, power

class TestSum(unittest.TestCase):
    
    def test_addingTestEqual(self):
        self.assertEqual(sum(3, 8), 11)
        
    def test_addingTestNotEqual(self):
        self.assertNotEqual(sum(2, 1), 6)

class TestProduct(unittest.TestCase):
    
    def test_multiplyingTestEqual(self):
        self.assertEqual(product(3, 8), 24)
        
    def test_multiplyingTestNotEqual(self):
        self.assertNotEqual(product(2, 1), 11)

class TestPower(unittest.TestCase):
    
    def test_multiplyingTestEqual(self):
        self.assertEqual(power(2, 10), 1024)
        
    def test_multiplyingTestNotEqual(self):
        self.assertNotEqual(power(2, 4), 64)                