import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def testEnglishToFrenchEqual(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def testEnglishToFrenchNotEqual(self):
        self.assertNotEqual(englishToFrench("Bonjour"), "Hello")
    def testEnglishToFrenchNull(self):
        self.assertRaises(ValueError, englishToFrench, None)
     
    def testFrenchToEnglishEqual(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    def testFrenchToEnglishNotEqual(self):
        self.assertNotEqual(frenchToEnglish("Hello"), "Bonjour")
    def testFrenchToEnglishNull(self):
        self.assertRaises(ValueError, frenchToEnglish, None)

unittest.main()
