import unittest
import os
import tempfile
from mcrack import time_format, get_total_lines, try_pdf, try_office

class TestMcrack(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
        self.test_file.write("line1\nline2\nline3\n")
        self.test_file.close()

    def tearDown(self):
        # Clean up the temporary file
        os.remove(self.test_file.name)

    # Test 1: Verify time formatting function
    def test_time_format(self):
        self.assertEqual(time_format(0), "00:00:00")
        self.assertEqual(time_format(65), "00:01:05")
        self.assertEqual(time_format(3661), "01:01:01")
        self.assertEqual(time_format(-10), "00:00:00")

    # Test 2: Verify line counting function
    def test_get_total_lines(self):
        count = get_total_lines(self.test_file.name)
        self.assertEqual(count, 3)
        self.assertEqual(get_total_lines("non_existent_file.txt"), 0)

    # Test 3: Verify PDF password checking (Mocked)
    def test_try_pdf_mock(self):
        result = try_pdf(self.test_file.name, "password")
        self.assertFalse(result)

    # Test 4: Verify Office password checking (Mocked)
    def test_try_office_mock(self):
        result = try_office(self.test_file.name, "password", ".docx")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
