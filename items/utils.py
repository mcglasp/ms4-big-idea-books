import random


def create_new_sku():
    return str(random.randint(1000000000, 9999999999))


def format_discount(discount):
    return discount / 100

    