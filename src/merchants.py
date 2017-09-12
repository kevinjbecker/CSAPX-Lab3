"""
This is just so I can commit properly
"""

import collections
from typing import List
from typing import Tuple
from sys import argv

Merchant = collections.namedtuple('Merchant',  ('merchant_name', 'merchant_location'))


def main()->None:
    merchants = quick_sort(read_merchants(argv[1]))
    for merchant in merchants:
        print(merchant.merchant_name, ' is located  at ', merchant.merchant_location)

    print('The median merchant is: ', merchants[len(merchants)//2].merchant_name, ' at location ', merchants[len(merchants)//2].merchant_location)


def read_merchants(filename: str) -> List[Merchant]:
    """
    Read Mer from a file into a list of Person namedtuples.
    :param filename: The name of the file
    :return: A list of Person
    """
    merchants = list()
    with open(filename) as f:
        for line in f:
            fields = line.split(' ')
            merchants.append(Merchant(
                merchant_name=fields[0],
                merchant_location=int(fields[1])
            ))
    return merchants


def _partition(data: List[Merchant], pivot: Merchant) -> Tuple[List[Merchant], List[Merchant], List[Merchant]]:
    """
    Three way partition the data into smaller, equal and greater lists,
    in relationship to the pivot
    :param data: The data to be sorted (a list)
    :param pivot: The value to partition the data on
    :return: Three list: smaller, equal and greater
    """
    less, equal, greater = [], [], []
    for element in data:
        if element.merchant_location < pivot.merchant_location:
            less.append(element)
        elif element.merchant_location > pivot.merchant_location:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater


def quick_sort(data: List[Merchant]) -> List[Merchant]:
    """
    Performs a quick sort and returns a newly sorted list
    :param data: The data to be sorted (a list)
    :return: A sorted list
    """
    if len(data) == 0:
        return []
    else:
        pivot = data[0]
        less, equal, greater = _partition(data, pivot)
        return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    main()