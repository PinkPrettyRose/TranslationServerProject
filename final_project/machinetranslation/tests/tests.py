import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertRaises(ValueError, englishToFrench, None)
     
    def testFrenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertRaises(ValueError, frenchToEnglish, None)

unittest.main()
