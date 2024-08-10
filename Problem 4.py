""" Problem 4: Write a Python function to validate the regular expression for the following:
               a) Email address
               b) Mobile number of Bangladesh
               c) Telephone number of USA
               d) Password : A 16-character alphanumeric password with upper case, lower case,
                             special characters and numbers"""



# Importing re module to work with regex expression
import re

# Created a class
class RegularExpression:

    # Function to validate email address
    def validate_email(self, email_id):
        """ Logic:  1) It is an alpha-numeric string
                    2) It should have @
                    3) Alphanumeric string on the LHS & RHS of @ symbol
                    4) A . symbol
                    5) A domain after the . symbol of either 2 to 6 character long """

        pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}"

        # Condition to check the pattern matches the input
        if re.match(pattern, email_id):
            return True
        else:
            return False

    # Function to validate mobile number of Bangladesh
    def validate_mobile_bangladesh(self, mobile_no):
        """ Logic:  (e.g., +880 XXXXXXXXXX)
                  1) It is of 13 digits only
                  2) Starts with +880
                  3) Followed by 10 digits, any digit between 0 to 9"""

        pattern = r"^\+880[0-9]{10}$"
        if re.match(pattern, mobile_no):
            return True
        else:
            return False

    # Function to validate Telephone number of USA
    def validate_telephone_usa(self, ph_no):
        """ Logic: (e.g., +1 (XXX) XXX-XXXX
                  1) +1 Country code for US in the start
                  2) 1st 3 digits will be country code
                  3) Next 7 digits will be local number."""

        pattern = r"^\+1[0-9]{3}[0-9]{7}$"
        if re.match(pattern, ph_no):
            return True
        else:
            return False

    # Function to validate password
    def validate_password(self, password):
        """ Logic: A 16-character alphanumeric password with upper case,
                   lower case, special characters, and numbers"""
        pattern = r"[A-Za-z%@$*._0-9]{16}$"
        if re.match(pattern, password):
            return True
        else:
            return False


# Code execution starts from here
if __name__ == "__main__":

    # Created an object for the class
    regex = RegularExpression()
    email_id = "abcd@google.in"

    # Using object, accessing functions in the class
    print(regex.validate_email(email_id))

    mobile_no = "+8808312345678"
    print(regex.validate_mobile_bangladesh(mobile_no))

    ph_no = "+14016783940"
    print(regex.validate_telephone_usa(ph_no))

    password = "Asdgt%*12345Yhir"
    print(regex.validate_password(password))
