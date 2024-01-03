from validators import ValidationError
import validators
import requests
import re

def url_valid(url):
    print("[+] - Validating URL")
    try:
        if not(validators.url(url)):
            raise ValidationError("Not a URL")
        response = requests.head(url)
        if not(response.status_code == 200):
            raise requests.exceptions.InvalidURL("Invalid URL")
        print("[+] - URL is Valid")
        return True
    except Exception as e:
        print("[-] - URL IS Invalid")
        return False
    