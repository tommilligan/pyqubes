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

class TestUtilsLinuxUsernameValidation(unittest.TestCase):
    def test_utils_linux_username_valid_simple(self):
        username = "foobar"
        valid_username = pyqubes.utils.validate_linux_username(username)
        self.assertTrue(valid_username)

    def test_utils_linux_username_valid_complex(self):
        username = "_f00-bar$"
        valid_username = pyqubes.utils.validate_linux_username(username)
        self.assertTrue(valid_username)

    def test_utils_linux_username_invalid_spaces(self):
        username = "foo bar"
        valid_username = pyqubes.utils.validate_linux_username(username)
        self.assertFalse(valid_username)

    def test_utils_linux_username_invalid_numeric(self):
        username = "1234foobar"
        valid_username = pyqubes.utils.validate_linux_username(username)
        self.assertFalse(valid_username)

    def test_utils_linux_username_invalid_length_zero(self):
        username = ""
        valid_username = pyqubes.utils.validate_linux_username(username)
        self.assertFalse(valid_username)

    def test_utils_linux_username_invalid_length_long(self):
        username = "fb" * 32
        valid_username = pyqubes.utils.validate_linux_username(username)
        self.assertFalse(valid_username)

