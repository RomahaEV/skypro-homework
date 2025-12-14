def filter_by_currency(transactions, currency):
    """
    Возвращает итератор по транзакциям с заданной валютой.

    :param transactions: список словарей с транзакциями
    :param currency: строка с кодом валюты (например, 'USD')
    :return: итератор
    """
    return (
        transaction
        for transaction in transactions
        if transaction.get("currency") == currency
    )

def transaction_descriptions(transactions):
    """
    Генератор, возвращающий описание каждой транзакции по очереди.

    :param transactions: список словарей с транзакциями
    :yield: строка с описанием операции
    """
    for transaction in transactions:
        description = transaction.get("description", "Описание отсутствует")
        yield description

def card_number_generator(start, end):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение (int)
    :param end: конечное значение (int)
    :yield: номер карты в виде строки
    """
    for number in range(start, end + 1):
        # Преобразуем число в строку из 16 цифр с ведущими нулями
        card_number = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted = " ".join(card_number[i:i+4] for i in range(0, 16, 4))
        yield formatted
