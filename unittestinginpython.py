import unittest

class Test(unittest.TestCase):
  
         
    def division(numberOne, numberTwo):
            result = numberOne/ numberTwo
            return result

    def test_number_division_success(self):
        result = Test.division(24, 12)
        self.assertEqual(result, 2)
    
    def test_number_division_different_number(self):
        result = Test.division(24, 12)
        self.assertNotEqual(result, 3)


if __name__ == '__main__' :
    unittest.main()