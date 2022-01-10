import unittest

from translator import frenchToEnglish, englishToFrench

class TestfrenchToEnglish(unittest.TestCase): 
    def test(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')  # test when 'Bonjour' is enter it returns 'Hello'.
        with self.assertRaises(TypeError):
            frenchToEnglish() 


class TestDouble(unittest.TestCase): 
    def test(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when 'Hello' is enter it returns 'Bonjour'.  
        with self.assertRaises(TypeError):
            englishToFrench() 
unittest.main()