import unittest

import tests.context


# Test case for the class
class Testapi(unittest.TestCase):

    def setUp(self):
        self.main = tests.context.main

    def test_tag(self):
        self.assertEqual(self.main.enclose("table", "th"), "<th>table</th>")


if __name__ == '__main__':
    unittest.main()
