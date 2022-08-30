import os
import unittest
from app import Receipt

class TestParseFields(unittest.TestCase):
    SAMPLES_PATH = 'samples/'

    def test_parse_date(self):
        # Get a list of files in the samples directory
        files = os.listdir(self.SAMPLES_PATH)

        # Loop through each file in the samples directory
        for file in files:
            # If the file is a .jpeg file, parse it
            if file.endswith('.jpeg'):
                receipt = Receipt(self.SAMPLES_PATH + file) 
                # Check the date matches the expected pattern
                self.assertRegexpMatches(receipt.get_date(), r'^\d{2}/\d{2}/\d{4}$')

    def test_parse_ncf(self):
        # Get a list of files in the samples directory
        files = os.listdir(self.SAMPLES_PATH)

        # Loop through each file in the samples directory
        for file in files:
            # If the file is a .jpeg file, parse it
            if file.endswith('.jpeg'):
                receipt = Receipt(self.SAMPLES_PATH + file)
                # Check the NCF matches the expected pattern
                self.assertRegexpMatches(receipt.get_ncf(), r'^B(\d){10}$')

    def test_parse_rnc(self):
        # Get a list of files in the samples directory
        files = os.listdir(self.SAMPLES_PATH)

        # Loop through each file in the samples directory
        for file in files:
            # If the file is a .jpeg file, parse it
            if file.endswith('.jpeg'):
                receipt = Receipt(self.SAMPLES_PATH + file)
                # Check the RNC matches the expected pattern
                self.assertRegexpMatches(receipt.get_rnc(), r'^(\d){9}$')

class TestParseFullReceipt(unittest.TestCase):
    SAMPLES_PATH = 'samples/'
    SAMPLE_RNC = 130389128

    def test_parse_full_receipt_01(self):
        receipt_name = 'receipt_01.jpeg'
        receipt = Receipt(self.SAMPLES_PATH + receipt_name)
        self.assertEqual(receipt.date, '26/08/2022')
        self.assertEqual(receipt.total, 530.00)
        self.assertEqual(receipt.subtotal, 530.00)
        self.assertEqual(receipt.total_tax, 80.86)
        self.assertEqual(receipt.rnc, self.SAMPLE_RNC)
        self.assertEqual(receipt.ncf, 'B0108383666')

    def test_parse_full_receipt_02(self):
        receipt_name = 'receipt_02.jpeg'
        receipt = Receipt(self.SAMPLES_PATH + receipt_name).as_dict()
        self.assertEqual(receipt.date, '23/08/2022')
        self.assertEqual(receipt.total, 530.00)
        self.assertEqual(receipt.subtotal, 530.00)
        self.assertEqual(receipt.total_tax, 80.86)
        self.assertEqual(receipt.rnc, self.SAMPLE_RNC)
        self.assertEqual(receipt.ncf, 'B0100417592')

if __name__ == '__main__':
    unittest.main()