#!/usr/bin/env python

import unittest

import pyqubes.compile


class TestCompileFlagsBoolean(unittest.TestCase):
    def test_compile_flags_boolean_simple(self):
        flags = {
            "--foo": True,
            "--bar": False
        }
        compiled_flags = pyqubes.compile.flags_boolean(flags)
        self.assertItemsEqual(compiled_flags, ["--foo"])

    def test_compile_flags_boolean_complex(self):
        flags = {
            "--foo": 1 != 1,
            "--bar": "spam",
            "--eggs": None,
        }
        compiled_flags = pyqubes.compile.flags_boolean(flags)
        self.assertItemsEqual(compiled_flags, ["--bar"])

    def test_compile_flags_boolean_empty(self):
        flags = {}
        compiled_flags = pyqubes.compile.flags_boolean(flags)
        self.assertItemsEqual(compiled_flags, [])

