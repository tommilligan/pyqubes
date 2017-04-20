#!/usr/bin/env python

import unittest

import pyqubes.validate


class TestvalidateLinuxUsername(unittest.TestCase):
    def test_validate_linux_username_valid_simple(self):
        username = "foobar"
        valid_username = pyqubes.validate.linux_username(username)
        self.assertTrue(valid_username)

    def test_validate_linux_username_valid_complex(self):
        username = "_f00-bar$"
        valid_username = pyqubes.validate.linux_username(username)
        self.assertTrue(valid_username)

    def test_validate_linux_username_invalid_spaces(self):
        username = "foo bar"
        valid_username = pyqubes.validate.linux_username(username)
        self.assertFalse(valid_username)

    def test_validate_linux_username_invalid_numeric(self):
        username = "1234foobar"
        valid_username = pyqubes.validate.linux_username(username)
        self.assertFalse(valid_username)

    def test_validate_linux_username_invalid_length_zero(self):
        username = ""
        valid_username = pyqubes.validate.linux_username(username)
        self.assertFalse(valid_username)

    def test_validate_linux_username_invalid_length_long(self):
        username = "fb" * 32
        valid_username = pyqubes.validate.linux_username(username)
        self.assertFalse(valid_username)

