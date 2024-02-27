import unittest
from sms_sender import validate_and_extract_phone_number, get_timezone_for_country_code, get_country_from_country_code

class TestSMSSender(unittest.TestCase):
    def test_validate_and_extract_phone_number_valid(self):
        phone_number = "+31123456789"
        country_code, national_number = validate_and_extract_phone_number(phone_number)
        self.assertIsInstance(country_code, int)
        self.assertIsInstance(national_number, str)

    def test_validate_and_extract_phone_number_no_plus_sign(self):
        phone_number = "1234567890"
        with self.assertRaises(ValueError) as context:
            validate_and_extract_phone_number(phone_number)
        self.assertTrue("must start with a '+' sign" in str(context.exception))

    def test_validate_and_extract_phone_number_invalid_format(self):
        phone_number = "+1abcdefg"
        with self.assertRaises(ValueError) as context:
            validate_and_extract_phone_number(phone_number)
        self.assertTrue("Invalid phone number format." in str(context.exception))

    def test_get_country_from_country_code_valid(self):
        country_code = 1  # Example for USA
        country = get_country_from_country_code(country_code)
        self.assertEqual(country, 'US')

    def test_get_timezone_for_country_code_valid(self):
        country_code = 1  # Example for USA
        timezone = get_timezone_for_country_code(country_code)
        self.assertTrue(isinstance(timezone, str))
        self.assertTrue(timezone.startswith('America/'))

    # Add more tests as needed for edge cases and other functionalities

if __name__ == '__main__':
    unittest.main()
