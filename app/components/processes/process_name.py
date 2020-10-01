from typing import Tuple
from components.organisms.get_name import get_last_or_first_name


def process_name() -> Tuple[str, str, str]:
    last_name = get_last_or_first_name()
    first_name = get_last_or_first_name(last_name=False)
    full_name = first_name + last_name

    return first_name, last_name, full_name
