#!/usr/bin/env python

import unittest
import sys

from mock import patch
import six

import pyqubes.echo

class TestEchoCallPatch(unittest.TestCase):
    def setUp(self):
        self.print_patch = patch.object(six, 'print_').start()
        self.addCleanup(patch.stopall)

    def test_echo_call_patch_list(self):
        pyqubes.echo.call(["foo", "bar"])
        self.print_patch.assert_called_once_with("foo", "bar", file=sys.stdout, flush=True)

    def test_echo_call_patch_string(self):
        pyqubes.echo.call("foo bar")
        self.print_patch.assert_called_once_with("foo bar", file=sys.stdout, flush=True)

    def test_echo_call_patch_stderr(self):
        stream = sys.stderr
        pyqubes.echo.call("foo bar", file=stream)
        self.print_patch.assert_called_once_with("foo bar", file=stream, flush=True)


class TestEchoCallStream(unittest.TestCase):
    def setUp(self):
        self.stream = six.StringIO()
        self.addCleanup(self.stream.close)

    def test_echo_call_stream_list(self):
        pyqubes.echo.call(["foo", "bar"], file=self.stream)
        self.assertEqual(self.stream.getvalue(), "foo bar\n")

    def test_echo_call_stream_string(self):
        pyqubes.echo.call("foo bar", file=self.stream)
        self.assertEqual(self.stream.getvalue(), "foo bar\n")

