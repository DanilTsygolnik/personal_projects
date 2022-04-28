import unittest
from get_file_name import *

class Test(unittest.TestCase):

    def setUp(self):
        self.input_no_file_name = ["https://"]
        self.input_with_file_name = ["https://", "-o", "my_name"]

    def test_output_name(self):
        self.assertEqual(get_file_name(self.input_no_file_name), "parse_result.html")
        self.assertEqual(get_file_name(self.input_with_file_name), "my_name.html")

if __name__ == "__main__":
    unittest.main()
