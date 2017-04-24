# HC Book Swap

HC Book Swap is a Django web application for exchanging textbooks at Hinsdale Central High School.

## Features Implemented

The following features will be implemented when the project is completed.

- Ability to add and crop book listing thumbnails
- Verification of ISBN numbers
- Ability to easily edit and remove listings
- Filtering of books by subject, condition, and price
- Search by ISBN, course name, and course ID
- Integration of Mailgun API for contacting sellers when users express interest in a listed book
- ReCaptcha integration for verification of forms
- Population script to generate Course objects from current year's textbook spreadsheet

## Getting Started

Set up a virtual environment

```
virtualenv venv
venv/Scripts/activate
```

Install requirements

```
pip install requirements.txt
```

Create a secrets.py file in hc_books and add the following information

```
MAILGUN_API_KEY = 'YourAPIKeyHere'
MAILGUN_SENDER_DOMAIN = 'YourDomainHere'
SECRET_KEY = 'YourSecretKey'
RECAPTCHA_PUBLIC_KEY = 'YourReCaptchaSiteKey'
RECAPTCHA_PRIVATE_KEY = 'YourReCaptchaSecretKey'
ALLOWED_HOSTS = []
```