import os
from os import path

from tests.fixture import test_data

from utils import get_sorting_list_dictionaries, load_data, get_sorting_date, get_sorting_data


def test_load_data():
    file_output = [
        {
            "date": "2018-08-26T10:50:58.294041",
            "id": 441945886,
            "state": "EXECUTED",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "id": 41428829,
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "state": "EXECUTED",
            "id": 939719570,
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "date": "2018-03-23T10:45:06.972075",
            "description": "Открытие вклада",
            "state": "EXECUTED",
            "id": 587085106,
            "to": "Счет 41421565395219882431"
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "state": "EXECUTED",
            "id": 142264268,
            "to": "Счет 75651667383060284188"
        },
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "state": "EXECUTED",
            "id": 873106923,
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "date": "2018-12-20T16:43:26.929246",
            "description": "Перевод организации",
            "state": "EXECUTED",
            "id": 214024827,
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366"
        }
    ]
    assert load_data('test_file.json') == file_output
    assert load_data(os.path.join('test_file.json'))


def test_get_sorting_list_dictionaries():
    assert get_sorting_list_dictionaries('test_file.json') == []
    assert get_sorting_list_dictionaries('test_file.json', filter_from=True) == []


def test_get_sorting_date(test_data):
    data = get_sorting_date(test_data)
    assert [item["date"] for item in data] == ["2019-09-03T18:35:29.512364", "2019-08-26T10:50:58.294041",
                                               "2018-06-30T02:08:58.425572", "2018-04-04T23:20:05.206878",
                                               "2018-03-23T10:45:06.972075"]


def test_get_sorting_data(test_data):
    data = get_sorting_data(test_data)
    assert data == ['03.09.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD',
                    '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.',
                    '30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD',
                    '04.04.2018 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD',
                    '23.03.2018 Открытие вклада\nno data  -> Счет **2431\n48223.05 руб.']
