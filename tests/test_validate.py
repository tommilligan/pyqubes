#!/usr/bin/env python

import unittest

import pyqubes.validate


class TestvalidateLinuxUsername(unittest.TestCase):
    def test_validate_linux_username_valid_simple(self):
        input_string = "foobar"
        valid_input_string = pyqubes.validate.linux_username(input_string)
        self.assertTrue(valid_input_string)

    def test_validate_linux_username_valid_complex(self):
        input_string = "_f00-bar$"
        valid_input_string = pyqubes.validate.linux_username(input_string)
        self.assertTrue(valid_input_string)

    def test_validate_linux_username_invalid_spaces(self):
        input_string = "foo bar"
        valid_input_string = pyqubes.validate.linux_username(input_string)
        self.assertFalse(valid_input_string)

    def test_validate_linux_username_invalid_numeric(self):
        input_string = "1234foobar"
        valid_input_string = pyqubes.validate.linux_username(input_string)
        self.assertFalse(valid_input_string)

    def test_validate_linux_username_invalid_length_zero(self):
        input_string = ""
        valid_input_string = pyqubes.validate.linux_username(input_string)
        self.assertFalse(valid_input_string)

    def test_validate_linux_username_invalid_length_long(self):
        input_string = "fb" * 32
        valid_input_string = pyqubes.validate.linux_username(input_string)
        self.assertFalse(valid_input_string)

class TestvalidateLinuxHostname(unittest.TestCase):
    def test_validate_linux_hostname_valid_simple(self):
        input_string = "foobar"
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertTrue(valid_input_string)

    def test_validate_linux_hostname_valid_complex(self):
        input_string = "edge.had-oop.1234-"
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertTrue(valid_input_string)

    def test_validate_linux_hostname_invalid_spaces(self):
        input_string = "foo bar"
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertFalse(valid_input_string)

    def test_validate_linux_hostname_invalid_period(self):
        input_string = "."
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertFalse(valid_input_string)

    def test_validate_linux_hostname_invalid_period(self):
        input_string = "trailing."
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertFalse(valid_input_string)

    def test_validate_linux_hostname_invalid_length_zero(self):
        input_string = ""
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertFalse(valid_input_string)

    def test_validate_linux_hostname_invalid_length_long(self):
        input_string = "fb" * 256
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertFalse(valid_input_string)

