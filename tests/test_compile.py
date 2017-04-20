#!/usr/bin/env python

import unittest

import six

import pyqubes.compile


class TestCompileFlagsBoolean(unittest.TestCase):
    def test_compile_flags_boolean_simple(self):
        flags = {
            "--foo": True,
            "--bar": False
        }
        compiled_flags = pyqubes.compile.flags_boolean(flags)
        six.assertCountEqual(self, compiled_flags, ["--foo"])

    def test_compile_flags_boolean_complex(self):
        flags = {
            "--foo": 1 != 1,
            "--bar": "spam",
            "--eggs": None,
        }
        compiled_flags = pyqubes.compile.flags_boolean(flags)
        six.assertCountEqual(self, compiled_flags, ["--bar"])

    def test_compile_flags_boolean_empty(self):
        flags = {}
        compiled_flags = pyqubes.compile.flags_boolean(flags)
        six.assertCountEqual(self, compiled_flags, [])

class TestCompileFlagsStore(unittest.TestCase):
    def test_compile_flags_store_single(self):
        flags = {
            "--foo": "eggs",
            "--bar": ""
        }
        compiled_flags = pyqubes.compile.flags_store(flags)
        self.assertEqual(compiled_flags, ["--foo", "eggs"])

    def test_compile_flags_store_multiple(self):
        flags = {
            "--foo": 42,
            "--bar": None,
            "--eggs": "rabbit",
        }
        compiled_flags = pyqubes.compile.flags_store(flags)
        self.assertEqual(len(compiled_flags), 4)
        compiled_flags_pairs = [compiled_flags[0:2], compiled_flags[2:4]]
        self.assertIn(["--foo", "42"], compiled_flags_pairs)
        self.assertIn(["--eggs", "rabbit"], compiled_flags_pairs)

    def test_compile_flags_store_empty(self):
        flags = {}
        compiled_flags = pyqubes.compile.flags_store(flags)
        six.assertCountEqual(self, compiled_flags, [])

class TestCompileFlagsStoreIterable(unittest.TestCase):
    def test_compile_flags_store_iterable_single(self):
        flags = {
            "--foo": ["eggs", "bacon"],
            "--bar": ""
        }
        compiled_flags = pyqubes.compile.flags_store_iterable(flags)
        self.assertEqual(compiled_flags, ["--foo", "eggs", "--foo", "bacon"])

    def test_compile_flags_store_iterable_single_empty(self):
        flags = {
            "--foo": [],
        }
        compiled_flags = pyqubes.compile.flags_store_iterable(flags)
        six.assertCountEqual(self, compiled_flags, [])

    def test_compile_flags_store_iterable_single_invalid(self):
        flags = {
            "--foo": 47,
        }
        with self.assertRaises(TypeError):
            compiled_flags = pyqubes.compile.flags_store_iterable(flags)

    def test_compile_flags_store_iterable_multiple(self):
        flags = {
            "--foo": [42, "life"],
            "--bar": None,
            "--eggs": "13",
        }
        compiled_flags = pyqubes.compile.flags_store_iterable(flags)
        self.assertEqual(len(compiled_flags), 8)
        compiled_flags_pairs = [compiled_flags[0:4], compiled_flags[4:8]]
        self.assertIn(["--foo", "42", "--foo", "life"], compiled_flags_pairs)
        self.assertIn(["--eggs", "1", "--eggs", "3"], compiled_flags_pairs)

    def test_compile_flags_store_iterable_empty(self):
        flags = {}
        compiled_flags = pyqubes.compile.flags_store_iterable(flags)
        six.assertCountEqual(self, compiled_flags, [])

