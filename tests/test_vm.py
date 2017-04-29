#!/usr/bin/env python

import unittest
import sys

from mock import patch

import pyqubes.enact
import pyqubes.vm

class TestVmAppVM(unittest.TestCase):
    def setUp(self):
        self.echo_patch = patch.object(pyqubes.enact, 'echo').start()
        self.call_patch = patch.object(pyqubes.enact, 'call').start()
        self.addCleanup(patch.stopall)

    def test_vm_app_vm_reactive(self):
        '''
        Reactive VMs should call ``echo`` only
        '''
        app_vm = pyqubes.vm.AppVM("reactive.spam")
        app_vm.enact(["foo", "bar"])
        self.echo_patch.assert_called_once_with(["foo", "bar"])
        self.call_patch.assert_not_called()

    def test_vm_app_vm_proactive(self):
        '''
        Reactive VMs should call ``call`` only
        '''
        app_vm = pyqubes.vm.AppVM("proactive.spam", proactive=True)
        app_vm.enact(["foo", "bar"])
        self.call_patch.assert_called_once_with(["foo", "bar"])
        self.echo_patch.assert_not_called()

