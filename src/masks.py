def get_mask_card_number(card: str) -> str:
    """
    Принимает номер карты (строка, возможно с пробелами) и возвращает маску.
    Видим первые 6 символов и последние 4, всё между заменено звёздочками.
    Результат форматируется в блоки по 4 символа, разделённые пробелом.
    """

    s = str(card)
    left_visible = s[:6]
    right_visible = s[12:16]
    masked = left_visible + "******" + right_visible

    # Разбиваем на блоки по 4 символа
    groups = [masked[i : i + 4] for i in range(0, len(masked), 4)]

    return " ".join(groups)


def get_mask_account(number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается
    в формате **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера, а
    перед ними — две звездочки."""

    check = str(number)
    masked = "**" + check[-4:]

    return masked
