import unittest
from bunq2ynab.converter import Converter
from pandas._libs.tslibs.timestamps import Timestamp
import pandas as pd


class TestConverter(unittest.TestCase):

    def test_inflow(self):
        """
        Test that inflow has been converted correctly
        """
        data = {'Date': {0: Timestamp('2021-01-01 00:00:00')},
                'Interest Date': {0: '2021-01-01'},
                'Amount': {0: 1000.0},
                'Account': {0: 'NL52BUNQ123'},
                'Counterparty': {0: 'NL22INGB123'},
                'Name': {0: 'test_name'},
                'Description': {0: 'test_description'}}
        df = pd.DataFrame(data)
        converter = Converter(data=df)
        converter.convert()

        self.assertEqual(converter.output_data['Inflow'][0], 1000.00)

    def test_outflow(self):
        """
        Test that outflow has been converted correctly
        """
        data = {'Date': {0: Timestamp('2021-01-01 00:00:00')},
                'Interest Date': {0: '2021-01-01'},
                'Amount': {0: -1000.0},
                'Account': {0: 'NL52BUNQ123'},
                'Counterparty': {0: 'NL22INGB123'},
                'Name': {0: 'test_name'},
                'Description': {0: 'test_description'}}
        df = pd.DataFrame(data)
        converter = Converter(data=df)
        converter.convert()

        self.assertEqual(converter.output_data['Outflow'][0], 1000.00)


if __name__ == '__main__':
    unittest.main()
