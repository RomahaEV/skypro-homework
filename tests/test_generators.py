import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [1, 3]),
        ("EUR", [2]),
    ],
)
def test_filter_by_currency_success(transactions, currency, expected_ids):
    result = list(filter_by_currency(transactions, currency))
    ids = [tx["id"] for tx in result]

    assert ids == expected_ids


def test_filter_by_currency_no_matches(transactions):
    result = list(filter_by_currency(transactions, "GBP"))
    assert result == []

def test_filter_by_currency_empty_list(empty_transactions):
    result = list(filter_by_currency(empty_transactions, "USD"))
    assert result == []

def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert result == ["Оплата", "Перевод", "Возврат"]

def test_transaction_descriptions_missing_description():
    transactions = [{"id": 1, "amount": 100, "currency": "USD"}]
    result = list(transaction_descriptions(transactions))

    assert result == ["Описание отсутствует"]

def test_transaction_descriptions_empty(empty_transactions):
    result = list(transaction_descriptions(empty_transactions))
    assert result == []

def test_card_number_generator_range():
    result = list(card_number_generator(1, 3))

    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]

@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "0000 0000 0000 0001"),
        (1234, "0000 0000 0000 1234"),
        (9999999999999999, "9999 9999 9999 9999"),
    ],
)
def test_card_number_format(number, expected):
    result = next(card_number_generator(number, number))
    assert result == expected

def test_card_number_generator_edges():
    result = list(card_number_generator(9999999999999998, 9999999999999999))

    assert result == [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]

def test_card_number_generator_stop():
    gen = card_number_generator(1, 1)
    next(gen)

    with pytest.raises(StopIteration):
        next(gen)