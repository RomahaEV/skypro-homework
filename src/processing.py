from typing import List, Dict, Any


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает список операций, у которых значение по ключу 'state'
    совпадает с указанным.

    :param operations: список операций
    :param state: статус для фильтрации
    :return: отфильтрованный список операций
    """
    filtered_operations = []
    for operation in operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по ключу 'date' в порядке убывания.

    :param operations: список операций
    :return: отсортированный список операций
    """
    sorted_operations = sorted(operations, key=lambda operation: operation["date"], reverse=True)
    return sorted_operations

# Пробное слияние в PR
