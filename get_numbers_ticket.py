# Task 2

import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    try:
        if min < 1:
            raise ValueError(f"Min: {min} should be equal or more than 1")
        elif max > 1000:
            raise ValueError(f"Max: {max} should be equal or less than 1000")
        elif min > max:
            raise ValueError(f"Max: {max} should be grater than Min: {min}")
        elif quantity < min or quantity > max:
            raise ValueError("Quantity should be greater than min and less than max")

        random_list = list(range(min, max + 1))
        numbers_ticket = sorted(random.sample(random_list, quantity))

        return numbers_ticket

    except (TypeError, ValueError) as err:
        print(f"Error: {err}")
        return []


print(get_numbers_ticket(30, 20, 400))
