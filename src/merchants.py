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
    if len(argv) > 3 or (len(argv) == 3 and (argv[1].lower() not in ['fast', 'slow'])):
        # if it gets here, too many commands were provided, tell user what proper command usage would be
        print('Usage: python3 merchants.py [slow|fast] input-file')

    else:
        # this reads in the merchants
        merchants = read_merchants(argv[len(argv) - 1])

        # gathers the number of merchants
        number_of_merchants = len(merchants)

        # gets into the nitty gritty of what's supposed to be happening
        start = clock()
        if argv[1] == 'slow':
            method = 'slow'
            quick_sorted_merchants = quick_sort(merchants)
            optimal = quick_sorted_merchants[len(merchants) // 2]
        else:
            method = 'fast'
            optimal = quick_select(merchants, len(merchants)//2)
        finish = clock() - start

        sum_of_distances = 0
        for merchant in merchants:
            sum_of_distances += abs(optimal.merchant_location - merchant.merchant_location)
        print('Search type:', method, '\nNumber of merchants:', number_of_merchants, '\nElapsed time:', finish,
              '\nOptimal store location:', optimal, '\nSum of distances:', sum_of_distances)


def read_merchants(filename: str) -> List[Merchant]:
    """
    Read Merchants from a file into a list of Merchants namedtuples.
    :param filename: The name of the file
    :return: A list of Merchant
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

    # partitions the lists into three lists: those of less, those of greater and those of less value in terms of location number

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

    # quick sort returns an empty list if the length of the data is 0
    if len(data) == 0:
        return []
    else:
        # the pivot is selected by random
        pivot = data[int(random() * len(data))]
        # the items are partitioned based on the pivot
        less, equal, greater = _partition(data, pivot)
        # recurses through until all are sorted
        return quick_sort(less) + equal + quick_sort(greater)


def quick_select(data: List[Merchant], k: int) -> Merchant:
    """
    Performs a quick select and returns the k-th smallest element (in this case it will always be the median element)
    :param data: The data to be selected upon (a list)
    :param k: The k-th element to find in the list.
    :return: A Merchant namedtuple which is the median element.
    """

    if len(data) == 1:
        # if the length of the data list is 1, we return data
        return data[0]

    # the pivot is selected
    pivot = data[int(random() * len(data))]
    # the elements are partitioned based on the pivot
    less, equal, greater = _partition(data, pivot)

    # this is used for the next set of conditionals
    count = len(equal)
    # the length of the less list is m
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