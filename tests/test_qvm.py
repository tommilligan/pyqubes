#!/usr/bin/env python

import unittest

import pyqubes.qvm


class TestQvmRun(unittest.TestCase):
    def test_qvm_run_simple(self):
        command_args = pyqubes.qvm.qvm_run("pear", "echo foobar")
        self.assertEqual(command_args, ["qvm-run", "pear", "echo foobar"])
    
    def test_qvm_run_flags(self):
        command_args = pyqubes.qvm.qvm_run("pear", "echo foobar", pass_io=True, tray=False)
        self.assertEqual(command_args, ["qvm-run", "pear", "echo foobar", "--pass-io"])
    
    def test_qvm_run_user(self):
        command_args = pyqubes.qvm.qvm_run("pear", "echo foobar", user="monty")
        self.assertEqual(command_args, ["qvm-run", "pear", "echo foobar", "--user", "monty"])
    
    def test_qvm_run_user_invalid(self):
        with self.assertRaises(ValueError):
            command_args = pyqubes.qvm.qvm_run("pear", "echo foobar", user="monty || bad")
    
    def test_qvm_run_exclude(self):
        command_args = pyqubes.qvm.qvm_run("pear", "echo foobar", exclude=["penguin", "rabbit"])
        self.assertEqual(command_args, ["qvm-run", "pear", "echo foobar", "--exclude", "penguin", "--exclude", "rabbit"])
    
    def test_qvm_run_exclude_invalid(self):
        with self.assertRaises(ValueError):
            command_args = pyqubes.qvm.qvm_run("pear", "echo foobar", exclude=["penguin", "rabbit || bad"])
    
class TestQvmFirewall(unittest.TestCase):
    def test_qvm_firewall_flags(self):
        command_args = pyqubes.qvm.qvm_firewall("pear", list_view=True)
        self.assertEqual(command_args, ["qvm-firewall", "pear", "--list"])
    
    def test_qvm_firewall_policy(self):
        command_args = pyqubes.qvm.qvm_firewall("pear", set_policy="allow")
        self.assertEqual(command_args, ["qvm-firewall", "pear", "--policy", "allow"])
    
    def test_qvm_firewall_policy_invalid(self):
        with self.assertRaises(ValueError):
            command_args = pyqubes.qvm.qvm_firewall("pear", set_policy="spam")
    
    def test_qvm_firewall_user_rule(self):
        pass
    
    def test_qvm_firewall_user_rule_invalid(self):
        pass
    
class TestQvmShutdown(unittest.TestCase):
    def test_qvm_shutdown_simple(self):
        command_args = pyqubes.qvm.qvm_shutdown("pear")
        self.assertEqual(command_args, ["qvm-shutdown", "pear"])
    
    def test_qvm_shutdown_flags(self):
        command_args = pyqubes.qvm.qvm_shutdown("pear", quiet=True)
        self.assertEqual(command_args, ["qvm-shutdown", "pear", "--quiet"])
        
    def test_qvm_shutdown_exclude(self):
        command_args = pyqubes.qvm.qvm_shutdown("pear", exclude=["penguin", "rabbit"])
        self.assertEqual(command_args, ["qvm-shutdown", "pear", "--exclude", "penguin", "--exclude", "rabbit"])

class TestQvmStart(unittest.TestCase):
    def test_qvm_start_simple(self):
        command_args = pyqubes.qvm.qvm_start("pear")
        self.assertEqual(command_args, ["qvm-start", "pear"])
    
    def test_qvm_start_flags(self):
        command_args = pyqubes.qvm.qvm_start("pear", quiet=True)
        self.assertEqual(command_args, ["qvm-start", "pear", "--quiet"])
    
    def test_qvm_start_config(self):
        pass

class TestQvmClone(unittest.TestCase):
    def test_qvm_clone_simple(self):
        command_args = pyqubes.qvm.qvm_clone("pear", "plum")
        self.assertEqual(command_args, ["qvm-clone", "pear", "plum"])
    
    def test_qvm_clone_flags(self):
        command_args = pyqubes.qvm.qvm_clone("pear", "plum", quiet=True)
        self.assertEqual(command_args, ["qvm-clone", "pear", "plum", "--quiet"])
    
    def test_qvm_clone_path(self):
        pass

