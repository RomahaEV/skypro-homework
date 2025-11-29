def get_mask_card_number(card_number: str) -> str:
    """
    Принимает номер карты (строка, возможно с пробелами) и возвращает маску.
    Видим первые 6 символов и последние 4, всё между заменено звёздочками.
    Результат форматируется в блоки по 4 символа, разделённые пробелом.
    """
    normalized_number = str(card_number).replace(" ", "")

    left_part = normalized_number[:6]
    right_part = normalized_number[-4:]
    masked_number = left_part + "******" + right_part

    grouped_number = [masked_number[index: index + 4] for index in range(0, len(masked_number), 4)]

    return " ".join(grouped_number)


def get_mask_account(account_number: str) -> str:
    """
    Принимает на вход номер счёта и возвращает его маску.
    Формат: **XXXX — видны только последние 4 цифры.
    """
    normalized_number = str(account_number)
    masked_number = "**" + normalized_number[-4:]

    return masked_number
