#!/usr/bin/env python

import unittest
import subprocess
import sys

from mock import patch
import six

import pyqubes.enact

class TestEnactEchoPatch(unittest.TestCase):
    def setUp(self):
        self.print_patch = patch.object(six, 'print_').start()
        self.addCleanup(patch.stopall)

    def test_enact_echo_patch_list(self):
        pyqubes.enact.echo(["foo", "bar"])
        self.print_patch.assert_called_once_with("foo", "bar", file=sys.stdout, flush=True)

    def test_enact_echo_patch_string(self):
        pyqubes.enact.echo("foo bar")
        self.print_patch.assert_called_once_with("foo bar", file=sys.stdout, flush=True)

    def test_enact_echo_patch_stderr(self):
        stream = sys.stderr
        pyqubes.enact.echo("foo bar", file=stream)
        self.print_patch.assert_called_once_with("foo bar", file=stream, flush=True)


class TestEnactEchoStream(unittest.TestCase):
    def setUp(self):
        self.stream = six.StringIO()
        self.addCleanup(self.stream.close)

    def test_enact_echo_stream_list(self):
        pyqubes.enact.echo(["foo", "bar"], file=self.stream)
        self.assertEqual(self.stream.getvalue(), "foo bar\n")

    def test_enact_echo_stream_string(self):
        pyqubes.enact.echo("foo bar", file=self.stream)
        self.assertEqual(self.stream.getvalue(), "foo bar\n")

class TestEnactCall(unittest.TestCase):
    def test_enact_call_list(self):
        return_value = pyqubes.enact.call(["echo", "spam"])
        self.assertEqual(return_value, 0)

    def test_enact_call_string(self):
        return_value = pyqubes.enact.call("echo")
        self.assertEqual(return_value, 0)

    def test_enact_call_error(self):
        with self.assertRaises(subprocess.CalledProcessError):
            return_value = pyqubes.enact.call(["cat", "/"])

    def test_enact_call_harmful(self):
        with self.assertRaises(OSError):
            return_value = pyqubes.enact.call("echo harmless || echo harmful")

