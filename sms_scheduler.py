from datetime import datetime, timedelta
import schedule
import time
import pytz


def next_target_time_in_timezone(timezone_str, hour, minute):
    timezone = pytz.timezone(timezone_str)
    now = datetime.now(timezone)
    next_target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if now.hour > hour or (now.hour == hour and now.minute >= minute):  # If it's past the target time, schedule for the next day
        next_target_time += timedelta(days=1)
    return next_target_time.astimezone(pytz.utc)


def send_sms_at_set_time(phone_number, message):
    # Placeholder function to simulate sending an SMS
    print(f"Sending SMS to {phone_number}: {message}")

def schedule_sms(phone_number, message, timezone_str, target_hour, target_minute, ):
    next_target_utc = next_target_time_in_timezone(timezone_str, target_hour, target_minute)
    delay_seconds = (next_target_utc - datetime.now(pytz.utc)).total_seconds()

    # Adjust the schedule to use the dynamic target time
    schedule_time = next_target_utc.strftime('%H:%M')
    print(f"Scheduling SMS to {phone_number} at {schedule_time} UTC")
    schedule.every().day.at(schedule_time).do(send_sms_at_set_time, phone_number=phone_number, message=message)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Example usage
if __name__ == "__main__":
    phone_number = "+31123456789"
    message = "Your daily reminder."
    country_code = +31
    target_hour = 15
    target_minute = 0
    timezone_str = 'Europe/Amsterdam'
    schedule_sms(phone_number, message, timezone_str, target_hour, target_minute)