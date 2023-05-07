import json
import operator
from datetime import datetime


def load_data(path):
    """Загружаем данные из файла json"""

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_sorting_list_dictionaries(data, filter_from=False):
    """Сортирует список словарей по state и from"""

    data = [d for d in data if "state" in d and d["state"] == "EXECUTED"] 
    if filter_from:
        data = [d for d in data if "from" in d]
    return data


def get_sorting_date(data):
    """Сортировка списка словарей по дате,
    вывод 5 последних операций"""

    data.sort(key = operator.itemgetter("date"), reverse=True)
    data = data[:5]
    return data


def get_sorting_data(data):
    """Сортирует список словарей по state и вывод нового формата списка словарей"""

    global from_bill, sender
    form_data = []
    for item in data:
        data = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = item["description"]
        recipient = f"{item['to'].split()[0]} **{item['to'][-4:]}"
        operations_amount = f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}"

        if "from" in item:
            sender = item["from"].split()
            from_bill = sender.pop(-1)

            if len(from_bill) == 16:
                from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
                from_info = " ".join(sender)
            else:
                from_bill = f"**{from_bill[-4:]}"
                from_info = " ".join(sender)

        else:
            from_info, from_bill = "no data", ""

        form_data.append(f"""\
{data} {description}
{from_info} {from_bill} -> {recipient}
{operations_amount}""")
    return form_data
