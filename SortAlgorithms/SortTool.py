import random
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from HeapSort import heap_sort
from QuickSort import quicksort
from BogoSort import bogo_sort
from RadixSort import radix_sort


class Sort:
    def __init__(self):
        self.algorithm = {
            "i": lambda data: insertion_sort(data),
            "s": lambda data: selection_sort(data),
            "m": lambda data: merge_sort(data),
            "h": lambda data: heap_sort(data),
            "q": lambda data: quicksort(data),
            "b": lambda data: bogo_sort(data),
            "r": lambda data: radix_sort(data),
            "0": lambda data: self.just_use_whatever_sort(data),
        }

    def sort(self, data, choice):
        choice = choice[0].lower()
        algorithm = self.algorithm[choice]
        return algorithm(data)

    def just_use_whatever_sort(self, data):
        return
