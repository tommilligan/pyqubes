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

