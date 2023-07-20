import unittest
from convert_millis import convert_milliseconds_to_duration
from convert_millis import convert_milliseconds_to_date

class TestConvertMillisecondsToDuration(unittest.TestCase):

    def test_convert_milliseconds_zero(self):
        self.assertEqual(convert_milliseconds_to_duration(0), "0 seconds")

    def test_convert_milliseconds_seconds(self):
        self.assertEqual(convert_milliseconds_to_duration(5000), "5 seconds")

    def test_convert_milliseconds_minutes(self):
        self.assertEqual(convert_milliseconds_to_duration(150000), "2 minutes, 30 seconds")

    def test_convert_milliseconds_hours(self):
        self.assertEqual(convert_milliseconds_to_duration(7500000), "2 hours, 5 minutes")

    def test_convert_milliseconds_days(self):
        self.assertEqual(convert_milliseconds_to_duration(172800000), "2 days")

    def test_convert_milliseconds_large_value(self):
        self.assertEqual(convert_milliseconds_to_duration(9999999999), "115 days, 17 hours, 46 minutes, 39 seconds")
        
class TestConvertMillisecondsToDate(unittest.TestCase):
    
    def test_convert_milliseconds_to_date(self):
        self.assertEqual(convert_milliseconds_to_date(1500000000), "1970-01-18 00:40:00")

unittest.main()