import unittest

class Test(unittest.TestCase):
  
         
   # def division(numberOne, numberTwo):
   #         result = numberOne/ numberTwo
   #         return result

   # def test_number_division_success(self):
   #     result = Test.division(24, 12)
   #     self.assertEqual(result, 2)
    
   # def test_number_division_different_number(self):
   #     result = Test.division(24, 12)
   #     self.assertNotEqual(result, 3)

    def is_empty(word):
        if(len(word)==0):
            return True
        else:
            return False
          
    def test_is_empty_string_successful(self):
        result = Test.is_empty("")
        self.assertTrue(result, True)
        
    def test_is_empty_with_string_successful(self):
        result = Test.is_empty("")
        self.assertFalse(result, True)
 


if __name__ == '__main__' :
    unittest.main()
