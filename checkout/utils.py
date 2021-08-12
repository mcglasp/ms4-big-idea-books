import random


def create_order_number():

    number = str(random.randint(1000000000, 9999999999))
    order_num = f'ORDER{number}'

    return order_num
