from datetime import datetime
from random import random

__author__ = 'Shafikur Rahman'


def generate_random_number():
    now = datetime.now()
    generated_number = ''
    generated_number += now.microsecond
    generated_number += now.second
    generated_number += now.minute
    generated_number += now.hour
    generated_number += now.day
    generated_number += now.month
    generated_number += now.year

    try:
        generated_number = int(generated_number)
    except ValueError:
        generated_number = random.range(10000000, 99999999)
    return generated_number
