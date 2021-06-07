from typing import List

counts = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
test_case = ["A", "B", 'X']


def stock_list(stock_list: List[str], test_case):
    stock_dict = {}

    for stock in stock_list:
        stock_id, count = stock.split(' ')
        current_quantity = stock_dict.get(stock_id[0], 0) + int(count)
        stock_dict[stock_id[0]] = current_quantity

    result = []
    for k, v in stock_dict.items():
        if k in stock_dict.keys():
            result.append(f'({k} : {v})')
        else:
            result.append(f'({k} : {0})')

    result = ' - '.join(result)

    if result == result:
        print('Hurray')

    print(result)

    return result


if __name__ == "__main__":
    print(stock_list(counts, test_case))
