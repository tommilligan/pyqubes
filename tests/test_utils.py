#!/usr/bin/env python

import unittest

import logging

import pyqubes.utils

class FooBar(object):
    pass

class TestUtilsObjectHelpers(unittest.TestCase):
    def setUp(self):
        self.test_object = FooBar()

    def test_utils_object_fullname(self):
        test_object_fullname = pyqubes.utils.object_fullname(self.test_object)
        self.assertEqual(test_object_fullname, "tests.test_utils.FooBar")
    
    def test_utils_object_logger(self):
        test_object_logger = pyqubes.utils.object_logger(self.test_object)
        self.assertIsInstance(test_object_logger, logging.Logger)
        self.assertEqual(test_object_logger.name, "tests.test_utils.FooBar")

class TestUtilsAssertListItemsEqualInNested(unittest.TestCase):
    def setUp(self):
        self.expected_list = ['a', 'z', 'b']

    def test_utils_assert_list_items_equal_in_nested_sorted(self):
        test_nested = [['a', 'z', 'b'], [1, 2, 3]]
        pyqubes.utils.assert_list_items_equal_in_nested(test_nested, self.expected_list)

    def test_utils_assert_list_items_equal_in_nested_unsorted(self):
        test_nested = [[1, 2, 3], ['b', 'z', 'a']]
        pyqubes.utils.assert_list_items_equal_in_nested(test_nested, self.expected_list)

    def test_utils_assert_list_items_equal_in_nested_missing(self):
        test_nested = [[1, 2, 3], ['X', 'X', 'X']]
        with self.assertRaises(AssertionError):
            pyqubes.utils.assert_list_items_equal_in_nested(test_nested, self.expected_list)

    def test_utils_assert_list_items_equal_in_nested_duplicates(self):
        test_nested = [[1, 2, 3], ['a', 'z', 'b', 'b', 'b']]
        with self.assertRaises(AssertionError):
            pyqubes.utils.assert_list_items_equal_in_nested(test_nested, self.expected_list)

    def test_utils_assert_list_items_equal_in_nested_multiples(self):
        test_nested = [['a', 'z', 'b'], [1, 2, 3], ['a', 'z', 'b'], ['a', 'z', 'b']]
        pyqubes.utils.assert_list_items_equal_in_nested(test_nested, self.expected_list)

