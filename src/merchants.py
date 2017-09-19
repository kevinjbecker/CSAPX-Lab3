"""
This is just so I can commit properly
"""

import collections
from typing import List
from typing import Tuple
from random import random
from sys import argv
from time import clock

Merchant = collections.namedtuple('Merchant',  ('merchant_name', 'merchant_location'))


def main()->None:
    merchants = read_merchants(argv[1])

    start = clock()
    median_merchant = quick_select(merchants, len(merchants)//2)
    end = clock() - start

    print(median_merchant, end)


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


def quick_select(data: List[Merchant], k: int) -> Merchant:
    """
    Performs a quick select and returns the k-th smallest element (in this case it will always be the median element)
    :param data: The data to be selected upon (a list)
    :param k: The k-th element to find in the list.
    :return: A Merchant namedtuple which is the median element.
    """

    if len(data) == 1:
        return data[0]

    pivot = data[int(random() * len(data))]
    less, equal, greater = _partition(data, pivot)

    # this is used for the next set of conditionals
    count = len(equal)
    m = len(less)

    # if m is less than k and k is less than m+count, we know that the pivot is the k-th element
    if m <= k <= m+count:
        return pivot
    # if m is greater than k, we must run quick_select again on the less list
    elif m > k:
        return quick_select(less, k)
    # if we get here, we must run quick_select on the greater list
    else:
        return quick_select(greater, k-m-count)



if __name__ == "__main__":
    main()