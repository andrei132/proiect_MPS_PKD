from src.fileReader import FileReader
import unittest
import tempfile
import os


class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.temp_file.write("Otsu,0,0\nMean,0,0\nMedian,0,0\n")
        self.temp_file.close()

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_csv_read_with_first_line(self):
        reader = FileReader(self.temp_file.name)
        reader.csv_read()
        result = reader.get_result()
        expected_result = [['Mean', '0', '0'], ['Median', '0', '0']]
        self.assertEqual(result, expected_result)

    def test_csv_read_without_first_line(self):
        reader = FileReader(self.temp_file.name, need_first_line=False)
        reader.csv_read()
        result = reader.get_result()
        expected_result = [["Mean", "0", "0"], ["Median", "0", "0"]]
        self.assertEqual(result, expected_result)

    def test_get_line(self):
        reader = FileReader(self.temp_file.name)
        reader.csv_read()

        line = reader.get_line(1)
        expected_line = ["Median", "0", "0"]
        self.assertEqual(line, expected_line)

    def test_get_column(self):
        reader = FileReader(self.temp_file.name)
        reader.csv_read()

        column = reader.get_collumn(1)
        expected_column = ["0", "0"]
        self.assertEqual(column, expected_column)

    def test_get_element(self):
        reader = FileReader(self.temp_file.name)
        reader.csv_read()
        element = reader.get_element(1, 1)
        expected_element = 0.0
        self.assertEqual(element, expected_element)



if __name__ == '__main__':
    unittest.main()