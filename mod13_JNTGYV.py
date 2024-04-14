import unittest
from datetime import datetime

class TestInputs(unittest.TestCase):
    def test_symbol(self):
        # symbol: capitalized, 1-7 alpha characters
        valid_symbols = ["IBM", "GOOGL", "NASDAQ", "TOY", "ALPHA"]
        bad_symbols = ["ibm", "GOO21", "NASDAQ!", "TOY12345", "@lph@"]

        for symbol in valid_symbols:
            self.assertTrue(symbol.isalpha() and symbol.isupper() and len(symbol) <= 7)

        for symbol in bad_symbols:
            self.assertFalse(symbol.isalpha() and symbol.isupper() and len(symbol) <= 7)

    def test_chart_type(self):
        # chart type: 1 numeric character, 1 or 2
        valid_chart_types = ["1", "2"]
        bad_chart_types = ["3", "A", "b", "C", "0"]

        for chart_type in valid_chart_types:
            self.assertTrue(chart_type.isdigit() and chart_type in ["1", "2"])

        for chart_type in bad_chart_types:
            self.assertFalse(chart_type.isdigit() and chart_type in ["1", "2"])

    def test_time_series(self):
        # time series: 1 numeric character, 1 - 4
        valid_time_series = ["1", "2", "3", "4"]
        bad_time_series = ["0", "5", "a"]

        for time_series in valid_time_series:
            self.assertTrue(time_series.isdigit() and 1 <= int(time_series) <= 4)

        for time_series in bad_time_series:
            self.assertFalse(time_series.isdigit() and 1 <= int(time_series) <= 4)

    def test_start_date(self):
        # start date: date type YYYY-MM-DD
        valid_start_date = ["2006-12-30", "2019-08-10", "1945-04-30"]
        bad_start_date = ["2001/01/01", "01-01-2001", "2077-13-01"]

        for date in valid_start_date:
            self.assertTrue(self.is_valid_date_format(date))

        for date in bad_start_date:
            self.assertFalse(self.is_valid_date_format(date))

    def test_end_date(self):
        # end date: date type YYYY-MM-DD
        valid_end_date = ["2006-12-30", "2019-08-10", "1945-04-30"]
        bad_end_date = ["2001/01/01", "01-01-2001", "2077-13-01"]

        for date in valid_end_date:
            self.assertTrue(self.is_valid_date_format(date))

        for date in bad_end_date:
            self.assertFalse(self.is_valid_date_format(date))

    def is_valid_date_format(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    unittest.main()
