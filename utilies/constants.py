from enum import Enum


class ConstantStrings(str, Enum):
    # Constants strings
    EMAIL_TITLE = "Medsta email verification."

class ConstantVariables():
    EMAIL_OTP_LENGTH = 6