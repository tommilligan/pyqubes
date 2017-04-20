#!/usr/bin/env python

import unittest

import pyqubes.qvm


class TestQvmRun(unittest.TestCase):
    def test_qvm_run_simple(self):
        command_args = pyqubes.qvm.qvm_run("echo foobar")
        self.assertEqual(command_args, ["qvm-run", "echo foobar"])
    
    def test_qvm_run_flags(self):
        command_args = pyqubes.qvm.qvm_run("echo foobar", pass_io=True)
        self.assertEqual(command_args, ["qvm-run", "echo foobar", "--pass-io"])
    
    def test_qvm_run_user(self):
        command_args = pyqubes.qvm.qvm_run("echo foobar", user="monty")
        self.assertEqual(command_args, ["qvm-run", "echo foobar", "--user", "monty"])
    

