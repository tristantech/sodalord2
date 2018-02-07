
#
# Regular expressions for validating names, usernames, etc
#
REGEX_USERNAME = r"^[a-z0-9_]{1,20}$"
REGEX_NAME = r"^[A-Za-z\ \-]{1,100}$"
REGEX_EMAIL = r"^[A-Za-z\.\-\_]+@[A-Z0-9\.\-]+$"