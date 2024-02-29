# Timezone-Aware SMS Scheduler

A Python application that schedules and sends SMS messages to recipients at a specified local time, taking into account the recipient's timezone. This is particularly useful for applications needing to send notifications or reminders at specific times of the day across different time zones.

## Features

- Validates input phone numbers and extracts country codes.
- Determines the recipient's timezone based on the country code.
- Schedules SMS messages at a specified time in the recipient's local timezone.
- Flexible scheduling options, allowing for any target time.
- Utilizes `pytz` for timezone calculations and `schedule` for task scheduling.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed.
- Access to an SMS sending service (e.g., Twilio, Nexmo) for sending SMS messages.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/drexlar5/Timezone-Aware-SMS-Scheduler.git
