from random import choices, randint
from string import ascii_letters, digits
import base64
import cv2

account_chars = digits + ascii_letters

def _random_account_id():
    return ''.join(choices(account_chars, k=12))

def _random_amount():
    return randint(100, 100000) / 100

def create_random_transaction():
    return {
        "source": _random_account_id(),
        "target": _random_account_id(),
        "amount": _random_amount(),
        "currency": "BRZ",
    }
