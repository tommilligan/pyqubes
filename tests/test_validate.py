#!/usr/bin/env python

import unittest

import pyqubes.validate


class TestvalidateLinuxUsername(unittest.TestCase):
    def test_validate_linux_username_valid_simple(self):
        input_string = "foobar"
        valid_input_string = pyqubes.validate.linux_username(input_string)
        self.assertEqual(valid_input_string, input_string)

    def test_validate_linux_username_valid_complex(self):
        input_string = "_f00-bar$"
        valid_input_string = pyqubes.validate.linux_username(input_string)
        self.assertEqual(valid_input_string, input_string)

    def test_validate_linux_username_invalid_spaces(self):
        input_string = "foo bar"
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_username(input_string)

    def test_validate_linux_username_invalid_numeric(self):
        input_string = "1234foobar"
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_username(input_string)

    def test_validate_linux_username_invalid_length_zero(self):
        input_string = ""
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_username(input_string)

    def test_validate_linux_username_invalid_length_long(self):
        input_string = "fb" * 32
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_username(input_string)

class TestvalidateLinuxHostname(unittest.TestCase):
    def test_validate_linux_hostname_valid_simple(self):
        input_string = "foobar"
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertEqual(valid_input_string, input_string)

    def test_validate_linux_hostname_valid_complex(self):
        input_string = "edge.had-oop.1234-"
        valid_input_string = pyqubes.validate.linux_hostname(input_string)
        self.assertEqual(valid_input_string, input_string)

    def test_validate_linux_hostname_invalid_spaces(self):
        input_string = "foo bar"
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_hostname(input_string)

    def test_validate_linux_hostname_invalid_period(self):
        input_string = "."
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_hostname(input_string)

    def test_validate_linux_hostname_invalid_trailing(self):
        input_string = "trailing."
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_hostname(input_string)

    def test_validate_linux_hostname_invalid_length_zero(self):
        input_string = ""
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_hostname(input_string)

    def test_validate_linux_hostname_invalid_length_long(self):
        input_string = "fb" * 256
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.linux_hostname(input_string)

class TestvalidateFirewallPolicy(unittest.TestCase):
    def test_validate_firewall_policy_valid_allow(self):
        input_string = "allow"
        valid_input_string = pyqubes.validate.firewall_policy(input_string)
        self.assertEqual(valid_input_string, input_string)

    def test_validate_firewall_policy_valid_deny(self):
        input_string = "deny"
        valid_input_string = pyqubes.validate.firewall_policy(input_string)
        self.assertEqual(valid_input_string, input_string)

    def test_validate_firewall_policy_invalid_string(self):
        input_string = "fooxbar"
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.firewall_policy(input_string)

    def test_validate_firewall_policy_invalid_length_zero(self):
        input_string = ""
        with self.assertRaises(ValueError):
            valid_input_string = pyqubes.validate.firewall_policy(input_string)

