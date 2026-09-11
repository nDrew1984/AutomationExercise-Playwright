import random

base_url = "https://automationexercise.com/"

# login page
login_email = "testUser1111@email.com"
login_password = "pass123"
signup_name = "TestUser" + str(random.randint(1000, 9999))
signup_email = "testUser" + str(random.randint(1000, 9999)) + "@email.com"

# signup page - mandatory fields
signup_password = "pass" + str(random.randint(1000, 9999))
signup_first_name = "UserFirstName"
signup_last_name = "UserLastName"
signup_address = "Test Address"
signup_Country = "Canada"
signup_state = "Test State"
signup_city = "Test City"
signup_zip_code = "ZC12345"
signup_mobile_number = "+1234567890"

# products page
products_count = 4

# Payment
name_on_card = "John Doe"
card_number = "1234567890"
cvc = "111"
expiration_month = "01"
expiration_year = "1000"

