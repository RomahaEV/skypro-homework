from typing import List, Dict, Any

def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает список словарей, у которых значение по ключу 'state'
    совпадает с указанным.
    """
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.
    """
    sorted_data = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_data
