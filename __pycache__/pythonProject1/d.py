from sss import Student
import unittest


class test_string_methods(unittest.TestCase):

    def setup(self):
        pass
    def test_email(self):
        ted=Student('teja','loki',70)
        self.assertEqual(ted.email(),"tejaloki@gmail.com")

