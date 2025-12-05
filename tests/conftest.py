import pytest
from typing import List, Dict


@pytest.fixture
def sample_operations() -> List[Dict]:
    """
    Набор операций с различными статусами и датами.
    """
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18"},
        {"id": 2, "state": "CANCELED", "date": "2023-12-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-12T10:00:00"},
        {"id": 4, "state": "PENDING", "date": "2022-01-01T00:00:00"},
    ]


@pytest.fixture
def operations_with_same_dates() -> List[Dict]:
    """Операции с одинаковыми датами (для проверки стабильности сортировки)."""
    return [
        {"id": 10, "state": "EXECUTED", "date": "2024-03-11T02:26:18"},
        {"id": 11, "state": "EXECUTED", "date": "2024-03-11T02:26:18"},
        {"id": 12, "state": "CANCELED", "date": "2024-03-10T00:00:00"},
    ]


@pytest.fixture
def invalid_date_operations() -> List[Dict]:
    """Операции с нестандартными/плохими форматами дат (строки различной длины)."""
    return [
        {"id": 20, "state": "EXECUTED", "date": "20240311"},        # короткая строка
        {"id": 21, "state": "EXECUTED", "date": "2024/03/11"},     # другой разделитель
        {"id": 22, "state": "EXECUTED", "date": ""},              # пустая строка
    ]


@pytest.fixture
def sample_card_numbers() -> List[str]:
    """Разные варианты номеров карт для тестирования маскировки."""
    return [
        "2842878893689012",
        "2842 8788 9368 9012",  # с пробелами
        "1234",                 # короткий номер
        "",                     # пустая строка
    ]


@pytest.fixture
def sample_account_numbers() -> List[str]:
    """Разные варианты номеров счетов."""
    return [
        "40817810099910004312",
        "123",      # очень короткий
        "",         # пустая строка
    ]


@pytest.fixture
def raw_strings_for_mask_account_card() -> List[str]:
    """Разные входные строки для mask_account_card (карты и счета и некорректные)."""
    return [
        "Visa Classic 2842878893689012",
        "Счет 40817810099910004312",
        "MasterCard 5555666677778888",
        "Unknown 123",          # короткий номер
        "NoNumberHere",         # нет числа в конце
    ]