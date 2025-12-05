import pytest

from src.widget import  mask_account_card, get_date

@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Visa Classic 2842878893689012", "Visa Classic 2842 87** **** 9012"),
        ("Счет 40817810099910004312", "Счет **4312"),
        ("MasterCard 5555666677778888", "MasterCard 5555 66** **** 8888"),
    ],
)
def test_mask_account_card_recognizes_and_masks(input_string: str, expected: str):
    """Проверяем корректность маскирования для типичных случаев."""
    assert mask_account_card(input_string) == expected


@pytest.mark.parametrize(
    "date_input, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-01-01T00:00:00", "01.01.1999"),
        ("2024-03-11", "11.03.2024"),        # частичный формат — должно работать при срезах
        ("", ".."),                          # пустая строка — функция вернёт '..' по текущей реализации
    ],
)
def test_get_date_various_formats(date_input: str, expected: str):
    """Проверяем преобразование даты по нескольким форматам (включая странные)."""
    result = get_date(date_input)
    assert result == expected