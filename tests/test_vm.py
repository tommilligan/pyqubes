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

class TestVMVMBoundFunctions(unittest.TestCase):
    def setUp(self):
        self.enact_patch = patch.object(pyqubes.vm.VM, 'enact').start()
        self.addCleanup(patch.stopall)
        self.vm = pyqubes.vm.VM("bounding")

    def test_vm_vm_shutdown(self):
        self.vm.shutdown()
        self.enact_patch.assert_called_once_with(['qvm-shutdown', 'bounding', '--wait'])

    def test_vm_vm_start(self):
        self.vm.start()
        self.enact_patch.assert_called_once_with(['qvm-start', 'bounding'])

    def test_vm_vm_firewall(self):
        self.vm.firewall(list_view=True)
        self.enact_patch.assert_called_once_with(['qvm-firewall', 'bounding', '--list'])

    def test_vm_vm_clone(self):
        self.vm.clone('rebounding', quiet=True)
        self.enact_patch.assert_called_once_with(['qvm-clone', 'bounding', 'rebounding', '--quiet'])

    def test_vm_vm_run(self):
        self.vm.run("echo 'foo bar'")
        self.enact_patch.assert_called_once_with(['qvm-run', 'bounding', '"echo \'foo bar\'"', '--pass-io'])

class TestVMVMInternet(unittest.TestCase):
    def setUp(self):
        self.enact_patch = patch.object(pyqubes.vm.VM, 'enact').start()
        self.addCleanup(patch.stopall)
        self.vm = pyqubes.vm.TemplateVM("networker")

    def test_vm_vm_internet_online(self):
        self.vm.internet_online()
        self.enact_patch.assert_called_once_with(['qvm-firewall', 'networker', '--policy', 'allow'])

    def test_vm_vm_internet_offline(self):
        self.vm.internet_offline()
        self.enact_patch.assert_called_once_with(['qvm-firewall', 'networker', '--policy', 'deny'])

class TestVMVMMagicInternet(unittest.TestCase):
    def setUp(self):
        self.enter_patch = patch.object(pyqubes.vm.VM, 'internet_online').start()
        self.exit_patch = patch.object(pyqubes.vm.VM, 'internet_offline').start()
        self.addCleanup(patch.stopall)
        self.vm = pyqubes.vm.TemplateVM("magic")

    def test_vm_vm_magic_internet(self):
        with self.vm.internet as inet:
            self.enter_patch.assert_called_once_with()
            self.exit_patch.assert_not_called()
        self.enter_patch.assert_called_once_with()
        self.exit_patch.assert_called_once_with()

class TestVMVMMagicSupervise(unittest.TestCase):
    def setUp(self):
        self.enter_patch = patch.object(pyqubes.vm.VM, 'start').start()
        self.exit_patch = patch.object(pyqubes.vm.VM, 'shutdown').start()
        self.addCleanup(patch.stopall)
        self.vm = pyqubes.vm.TemplateVM("magic")

    def test_vm_vm_magic_supervise(self):
        with self.vm.supervise as supervisor:
            self.enter_patch.assert_called_once_with()
            self.exit_patch.assert_not_called()
        self.enter_patch.assert_called_once_with()
        self.exit_patch.assert_called_once_with()

class TestVMTemplateVMUpdate(unittest.TestCase):
    def setUp(self):
        self.enact_patch = patch.object(pyqubes.vm.VM, 'enact').start()
        self.addCleanup(patch.stopall)

    def test_vm_template_vm_update_fedora(self):
        template_vm = pyqubes.vm.TemplateVM("fedora.spam")
        template_vm.update()
        self.enact_patch.assert_called_once_with(['qvm-run', 'fedora.spam', '"sudo dnf check-update && sudo dnf -y upgrade"', '--pass-io'])

    def test_vm_template_vm_update_debian(self):
        template_vm = pyqubes.vm.TemplateVM("debian.spam", operating_system=pyqubes.constants.DEBIAN_8)
        template_vm.update()
        self.enact_patch.assert_called_once_with(['qvm-run', 'debian.spam', '"sudo apt-get update && sudo apt-get -y upgrade"', '--pass-io'])

    def test_vm_template_vm_update_invalid(self):
        with self.assertRaises(ValueError):
            template_vm = pyqubes.vm.TemplateVM("nonexistent.spam", operating_system='nonexistent')
            template_vm.update()

class TestVMAppVM(unittest.TestCase):
    def test_vm_app_vm(self):
        app_vm = pyqubes.vm.AppVM("stance")

