import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize(
    "card_input, expected_substrings",
    [
        ("2842878893689012", ("2842", "9012")),                     # стандартный
        ("2842 8788 9368 9012", ("2842", "9012")),                 # с пробелами
        ("1234", ("1234", "1234")),                                # короткий -> сохраняются видимые части
        ("", ("", "")),                                            # пустая строка -> возвращает строку (устойчиво)
    ],
)
def test_get_mask_card_number_properties(card_input: str, expected_substrings: tuple):
    """
    Проверяем, что функция возвращает строку и в ней видны ожидаемые части (первые/последние символы),
    а также что функция не падает на необычных входах.
    Точный формат для коротких строк может отличаться — проверяем свойства.
    """
    result = get_mask_card_number(card_input)
    assert isinstance(result, str)
    first_expected, last_expected = expected_substrings
    if first_expected:
        assert first_expected[:4] in result  # первые 4 символа должны присутствовать, если они есть
    if last_expected:
        assert last_expected[-4:] in result or last_expected in result


def test_get_mask_card_number_exact_format():
    """Проверяем строгое соответствие для известного корректного номера."""
    assert get_mask_card_number("2842878893689012") == "2842 87** **** 9012"


@pytest.mark.parametrize(
    "account_input, expected",
    [
        ("40817810099910004312", "**4312"),
        ("123", "**123"),  # короткий: берутся последние доступные символы
        ("", "**"),       # пустой: возвращает '**' + '' -> просто '**'
    ],
)
def test_get_mask_account(account_input: str, expected: str):
    result = get_mask_account(account_input)
    assert result == expected