def mask_account_card(source_string: str) -> str:
    """
    Функция, которая обрабатывает информацию как о картах, так и о счетах.
    Определяет тип по наличию слова «счет» и маскирует номер соответствующим образом.
    """
    parts = source_string.split()
    raw_number = parts[-1]
    description = " ".join(parts[:-1]).strip()
    is_account = "счет" in description.lower()
    if is_account:
        masked_number = "**" + raw_number[-4:]
    else:
        first_six_digits = raw_number[:6]
        last_four_digits = raw_number[-4:]
        masked_number = f"{first_six_digits[:4]} {first_six_digits[4:6]}** **** {last_four_digits}"
    return f"{description} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Принимает строку с датой в формате 'YYYY-MM-DDTHH:MM:SS'
    и возвращает строку 'DD.MM.YYYY'.
    """
    day = date_string[8:10]
    month = date_string[5:7]
    year = date_string[0:4]

    return f"{day}.{month}.{year}"
