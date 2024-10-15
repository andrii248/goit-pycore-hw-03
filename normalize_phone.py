# Task 3

import re


def normalize_phone(phone_number: str) -> str:
    pattern = r"[^\d+]+"
    stripped_number = re.sub(pattern, "", phone_number)

    if stripped_number.startswith("380"):
        stripped_number = "+" + stripped_number
    elif not stripped_number.startswith("+38"):
        stripped_number = "+38" + stripped_number

    return stripped_number
