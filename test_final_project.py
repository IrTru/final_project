import unittest
from methods_sort.bubble_sort import bubble_sort
from methods_sort.counting_sort import counting_sort
from methods_sort.merge_sort import merge_sort
from methods_sort.quick_sort import quick_sort
from methods_sort.radix_sort import radix_sort

# запускаем для тестирования
# python -m unittest

# Переменные для тестирования
list_test = [13,10,81,31,77]
list_end = [10,13,31,77,81]

class Tests_correct_methods(unittest.TestCase):

    def test_bubble_sort(self):
        assert(bubble_sort(list_test)) == list_end

    def test_counting_sort(self):
        assert(counting_sort(list_test)) == list_end

    def test_merge_sort(self):
        assert(merge_sort(list_test)) == list_end

    def test_quick_sort(self):
        assert(quick_sort(list_test)) == list_end

    def test_radix_sort(self):
        assert(radix_sort(list_test)) == list_end