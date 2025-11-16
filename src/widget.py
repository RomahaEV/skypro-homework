def mask_account_card(data: str) -> str:
    """
     Функция которая умеет обрабатывать информацию как о картах, так и о счетах.

    """
    parts = data.split()
    number = parts[-1]
    name = " ".join(parts[:-1])
    if "счет" in name.lower():
        masked_number = "**" + number[-4:]
    else:
        first6 = number[:6]
        last4 = number[-4:]
        masked_number = first6[:4] + " " + first6[4:6] + "** **** " + last4
    return name + " " + masked_number



def get_date(data_string: str) -> str:
    """
    которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате  "ДД.ММ.ГГГГ"
    """
    day = data_string[8:10]
    mouth = data_string[5:7]
    year = data_string[0:4]
    return f"{day}.{mouth}.{year}"


