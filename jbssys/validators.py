import re
import datetime


def validate_email(email):
    is_validate = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,8}$", email)
    is_validate = is_validate.group() if is_validate else ""
    return is_validate

def validate_firstname(name):
    if str(name).replace(" ", "").isalpha():
        return name
    else:
        return ""

def validate_phone(phone):
    phone = str(phone).replace("-","").replace('-',"")\
        .replace(".","").replace(" ","")\
        .replace("+","").replace("(","").replace(")","").replace("—","")

    phone_valid = re.search(r'^(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+$', phone)


    phone_valid = phone_valid.group() if phone_valid else ""
    return phone_valid


def validate_date(date_text):
    try:
        dtime = str(datetime.datetime.strptime(
            date_text, '%Y-%m-%d')
        ).split(" ")[0]

    except :

        dtime = ""

    return dtime
