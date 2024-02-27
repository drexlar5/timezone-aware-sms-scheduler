import phonenumbers
from phonenumbers import PhoneNumberFormat, geocoder
from sms_scheduler import schedule_sms
import pytz

def validate_and_extract_phone_number(phone_number):
    if not phone_number.startswith('+'):
        raise ValueError("Phone number must start with a '+' sign.")
    
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
    except phonenumbers.NumberParseException as e:
        raise ValueError("Invalid phone number format.") from e
    
    if not phonenumbers.is_valid_number(parsed_number):
        raise ValueError("Phone number is not valid.")
    
    country_code = parsed_number.country_code
    return country_code, str(parsed_number.national_number)

def get_country_from_country_code(country_code):
    return geocoder.region_code_for_country_code(country_code)

def get_timezone_for_country_code(country_code):
    timezones = pytz.country_timezones.get(get_country_from_country_code(country_code))
    if timezones:
        return timezones[0]
    else:
        raise ValueError("Timezone could not be determined from the country code.")

# Example usage
if __name__ == "__main__":
    phone_number = "+31123456789"
    try:
        country_code, national_number = validate_and_extract_phone_number(phone_number)
        timezone = get_timezone_for_country_code(country_code)
        message = "Good morning user"
        target_hour = 15  # 3 PM
        target_minute = 0
        timezone_str = get_timezone_for_country_code(country_code)
        print(f"Country Code: {country_code}, National Number: {national_number}, Timezone: {timezone}")
        schedule_sms(phone_number, message, timezone_str, target_hour, target_minute)
    except ValueError as e:
        print(e)
