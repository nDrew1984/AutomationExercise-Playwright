import time

# Search valid product
SEARCH_TERM_VALID = "Kids"

# Search non-existing product
SEARCH_TERM_NON_EXISTING = "nonExistingProduct"

# Creating Account
timestamp = time.time_ns() // 1000000
NAME = "TestName"
EMAIL = "testUser" + str(timestamp) + "@email.com"
PASSWORD = "pass111"
TITLE = "Mr"
BIRTH_DAY = "11"
BIRTH_MONTH = "10"
BIRTH_YEAR = "1970"
FIRSTNAME = "John"
LASTNAME = "Doe"
COMPANY = "TestCompany ltd."
ADDRESS1 = "testAddress1"
ADDRESS2 = "testAddress2"
COUNTRY = "Canada"
STATE = "TestState"
CITY = "TestCity"
ZIPCODE = "ZC 12345"
MOBILE_NUMBER = "+1234567890"

# Updating Account:
UPDATED_ADDRESS1 = ADDRESS1 + " UPDATED"
UPDATED_ADDRESS2 = ADDRESS2 + " UPDATED"
UPDATED_CITY = CITY + " UPDATED"
UPDATED_ZIPCODE = ZIPCODE + " UPDATED"
