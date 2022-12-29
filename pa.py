''''import unittest
import loki

class Testloki(unittest.TestCase):
    def test_add(self):
        self.assertEqual(loki.add(10,5),15)
        self.assertEqual(loki.add(15,4),19)


if __name__ == '__main__':
    unittest.main()'''''

import unittest
from loki import employee

class Testloki(unittest.TestCase):


    def test_email(self):
        emp_1=employee("teja","danda",50)
        self.assertEqual(emp_1.email,"tejadanda@email.com")







if __name__ == '__main__':
    unittest.main()
