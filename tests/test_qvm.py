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
    
    def test_qvm_run_user_invalid(self):
        with self.assertRaises(ValueError):
            command_args = pyqubes.qvm.qvm_run("echo foobar", user="monty || bad")
    
    def test_qvm_run_exclude(self):
        command_args = pyqubes.qvm.qvm_run("echo foobar", exclude=["penguin", "rabbit"])
        self.assertEqual(command_args, ["qvm-run", "echo foobar", "--exclude", "penguin", "--exclude", "rabbit"])
    
    def test_qvm_run_exclude_invalid(self):
        with self.assertRaises(ValueError):
            command_args = pyqubes.qvm.qvm_run("echo foobar", exclude=["penguin", "rabbit || bad"])
    
class TestQvmShutdown(unittest.TestCase):
    def test_qvm_shutdown_simple(self):
        command_args = pyqubes.qvm.qvm_shutdown("diaspora")
        self.assertEqual(command_args, ["qvm-shutdown", "diaspora"])
    
    def test_qvm_shutdown_flags(self):
        command_args = pyqubes.qvm.qvm_shutdown("diaspora", quiet=True)
        self.assertEqual(command_args, ["qvm-shutdown", "diaspora", "--quiet"])
        
    def test_qvm_shutdown_exclude(self):
        command_args = pyqubes.qvm.qvm_shutdown("diaspora", exclude=["penguin", "rabbit"])
        self.assertEqual(command_args, ["qvm-shutdown", "diaspora", "--exclude", "penguin", "--exclude", "rabbit"])
    

