#!/usr/bin/env python

import unittest
import sys

from mock import patch

import pyqubes.constants
import pyqubes.enact
import pyqubes.vm

class TestVmVmEnact(unittest.TestCase):
    def setUp(self):
        self.echo_patch = patch.object(pyqubes.enact, 'echo').start()
        self.call_patch = patch.object(pyqubes.enact, 'call').start()
        self.addCleanup(patch.stopall)

    def test_vm_vm_enact_reactive(self):
        '''
        Reactive VMs should call ``echo`` only
        '''
        vm = pyqubes.vm.VM("reactive.spam")
        vm.enact(["foo", "bar"])
        self.echo_patch.assert_called_once_with(["foo", "bar"])
        self.call_patch.assert_not_called()

    def test_vm_vm_enact_proactive(self):
        '''
        Reactive VMs should call ``call`` only
        '''
        vm = pyqubes.vm.VM("proactive.spam", proactive=True)
        vm.enact(["foo", "bar"])
        self.call_patch.assert_called_once_with(["foo", "bar"])
        self.echo_patch.assert_not_called()

class TestVMVMShutdown(unittest.TestCase):
    def setUp(self):
        self.enact_patch = patch.object(pyqubes.vm.VM, 'enact').start()
        self.addCleanup(patch.stopall)

    def test_vm_vm_shutdown(self):
        vm = pyqubes.vm.VM("sleepy")
        vm.shutdown()
        self.enact_patch.assert_called_once_with(['qvm-shutdown', 'sleepy', '--wait'])

class TestVMTemplateVMOnline(unittest.TestCase):
    def setUp(self):
        self.enact_patch = patch.object(pyqubes.vm.TemplateVM, 'enact').start()
        self.template_vm = pyqubes.vm.TemplateVM("networker")
        self.addCleanup(patch.stopall)

    def test_vm_template_vm_online(self):
        self.template_vm.go_online()
        self.enact_patch.assert_called_once_with(['qvm-firewall', 'networker', '--policy', 'allow'])

    def test_vm_template_vm_offline(self):
        self.template_vm.go_offline()
        self.enact_patch.assert_called_once_with(['qvm-firewall', 'networker', '--policy', 'deny'])

class TestVMTemplateVMUpdate(unittest.TestCase):
    def setUp(self):
        self.enact_patch = patch.object(pyqubes.vm.VM, 'enact').start()
        self.addCleanup(patch.stopall)

    def test_vm_template_vm_update_fedora(self):
        template_vm = pyqubes.vm.TemplateVM("fedora.spam")
        template_vm.update()
        self.enact_patch.assert_called_once_with(['qvm-run', 'fedora.spam', "'sudo dnf check-update && sudo dnf -y upgrade'", '--pass-io'])

    def test_vm_template_vm_update_debian(self):
        template_vm = pyqubes.vm.TemplateVM("debian.spam", operating_system=pyqubes.constants.DEBIAN_8)
        template_vm.update()
        self.enact_patch.assert_called_once_with(['qvm-run', 'debian.spam', "'sudo apt-get update && sudo apt-get -y upgrade'", '--pass-io'])

    def test_vm_template_vm_update_invalid(self):
        with self.assertRaises(ValueError):
            template_vm = pyqubes.vm.TemplateVM("nonexistent.spam", operating_system='nonexistent')
            template_vm.update()

class TestVMAppVM(unittest.TestCase):
    def test_vm_app_vm(self):
        app_vm = pyqubes.vm.AppVM("stance")

