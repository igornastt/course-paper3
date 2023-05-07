from utils import load_data, get_sorting_list_dictionaries, get_sorting_date, get_sorting_data
from os import path
import os

OPERATION_DATA_PATH = os.path.join("data", "operations.json")

def main():

    data = load_data(OPERATION_DATA_PATH)
    data = get_sorting_list_dictionaries(data, filter_from=False)
    data = get_sorting_date(data)
    data = get_sorting_data(data)

    for item in data:
        print(item, end="\n\n")



main()