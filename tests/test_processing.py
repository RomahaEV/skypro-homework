import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_operations):
    result = filter_by_state(sample_operations)
    assert all(op["state"] == "EXECUTED" for op in result)
    assert {op["id"] for op in result} == {1, 3}


@pytest.mark.parametrize("state_value, expected_ids", [
    ("CANCELED", {2}),
    ("PENDING", {4}),
    ("NOT_EXIST", set()),  # нет операций с таким статусом
])
def test_filter_by_state_various(sample_operations, state_value, expected_ids):
    result = filter_by_state(sample_operations, state=state_value)
    assert {op["id"] for op in result} == expected_ids


def test_sort_by_date_descending(sample_operations):
    result = sort_by_date(sample_operations)
    # Проверяем, что самая "поздняя" дата идёт первой
    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_stable_with_same_dates(operations_with_same_dates):
    result = sort_by_date(operations_with_same_dates)
    # При одинаковых датах порядок среди них должен сохраниться относительно stable sort
    ids_in_order = [op["id"] for op in result]
    assert ids_in_order[0:2] == [10, 11]  # элементы с одинаковой датой остаются в порядке появления


def test_sort_by_date_with_invalid_formats(invalid_date_operations):
    """
    Убедимся, что сортировка не бросает исключение при некорректных форматах дат.
    Проверяем просто, что функция вернула список той же длины.
    """
    result = sort_by_date(invalid_date_operations)
    assert isinstance(result, list)
    assert len(result) == len(invalid_date_operations)