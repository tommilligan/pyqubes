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
        compiled_args = pyqubes.compile.flags_boolean(flags)
        six.assertCountEqual(self, compiled_args, ["--foo"])

    def test_compile_flags_boolean_complex(self):
        flags = {
            "--foo": 1 != 1,
            "--bar": "spam",
            "--eggs": None,
        }
        compiled_args = pyqubes.compile.flags_boolean(flags)
        six.assertCountEqual(self, compiled_args, ["--bar"])

    def test_compile_flags_boolean_empty(self):
        flags = {}
        compiled_args = pyqubes.compile.flags_boolean(flags)
        six.assertCountEqual(self, compiled_args, [])

class TestCompileFlagsStore(unittest.TestCase):
    def test_compile_flags_store_single(self):
        flags = {
            "--foo": "eggs",
            "--bar": ""
        }
        compiled_args = pyqubes.compile.flags_store(flags)
        self.assertEqual(compiled_args, ["--foo", "eggs"])

    def test_compile_flags_store_multiple(self):
        flags = {
            "--foo": 42,
            "--bar": None,
            "--eggs": "rabbit",
        }
        compiled_args = pyqubes.compile.flags_store(flags)
        self.assertEqual(len(compiled_args), 4)
        compiled_args_pairs = [compiled_args[0:2], compiled_args[2:4]]
        self.assertIn(["--foo", "42"], compiled_args_pairs)
        self.assertIn(["--eggs", "rabbit"], compiled_args_pairs)

    def test_compile_flags_store_empty(self):
        flags = {}
        compiled_args = pyqubes.compile.flags_store(flags)
        six.assertCountEqual(self, compiled_args, [])

class TestCompileFlagsStoreIterable(unittest.TestCase):
    def test_compile_flags_store_iterable_single(self):
        flags = {
            "--foo": ["eggs", "bacon"],
            "--bar": ""
        }
        compiled_args = pyqubes.compile.flags_store_iterable(flags)
        self.assertEqual(compiled_args, ["--foo", "eggs", "--foo", "bacon"])

    def test_compile_flags_store_iterable_single_empty(self):
        flags = {
            "--foo": [],
        }
        compiled_args = pyqubes.compile.flags_store_iterable(flags)
        six.assertCountEqual(self, compiled_args, [])

    def test_compile_flags_store_iterable_single_invalid(self):
        flags = {
            "--foo": 47,
        }
        with self.assertRaises(TypeError):
            compiled_args = pyqubes.compile.flags_store_iterable(flags)

    def test_compile_flags_store_iterable_multiple(self):
        flags = {
            "--foo": [42, "life"],
            "--bar": None,
            "--eggs": "13",
        }
        compiled_args = pyqubes.compile.flags_store_iterable(flags)
        self.assertEqual(len(compiled_args), 8)
        compiled_args_pairs = [compiled_args[0:4], compiled_args[4:8]]
        self.assertIn(["--foo", "42", "--foo", "life"], compiled_args_pairs)
        self.assertIn(["--eggs", "1", "--eggs", "3"], compiled_args_pairs)

    def test_compile_flags_store_iterable_empty(self):
        flags = {}
        compiled_args = pyqubes.compile.flags_store_iterable(flags)
        six.assertCountEqual(self, compiled_args, [])

class TestCompileInfo(unittest.TestCase):
    def setUp(self):
        self.info = 'Flying circus'

    def test_compile_info(self):
        compiled_args = pyqubes.compile.info(self.info)
        self.assertEqual(compiled_args, ['echo', '-e', "'\\e[36mpyqubes|Flying circus\\e[39m'"])

    def test_compile_info_no_quote(self):
        compiled_args = pyqubes.compile.info(self.info, quote=False)
        self.assertEqual(compiled_args, ['echo', '-e', "\\e[36mpyqubes|Flying circus\\e[39m"])

    def test_compile_info_no_style(self):
        compiled_args = pyqubes.compile.info(self.info, style=False)
        self.assertEqual(compiled_args, ['echo', '-e', "'pyqubes|Flying circus'"])

