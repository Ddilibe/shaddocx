from validators import ValidationError
import validators
import requests
import re

def url_valid(url):
    try:
        if not(validators.url(url)):
            raise ValidationError("Not a URL")
        response = requests.head(url)
        if not(response.status_code == 200):
            raise requests.exceptions.InvalidURL("Invalid URL")
        return True, "No error"
    except Exception as e:
        return False, str(e)
    