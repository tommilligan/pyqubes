
import pyqubes.constants
import pyqubes.enact
import pyqubes.qvm
import pyqubes.validate


class InternetConnection(object):
    def __init__(self, vm):
        self.vm = vm

    def __enter__(self):
        self.vm.internet_online()

    def __exit__(self, type, value, traceback):
        self.vm.internet_offline()

class VM(object):
    def __init__(self, name, proactive=False, operating_system=pyqubes.constants.FEDORA_23):
        '''
        The VM object represants a QubesOS VM. Its methods are common accross
        both AppVMs and TemplateVMs.

        VM should not be instanciated directly - use TemplateVM or AppVM.

        By default, all VMs are Fedora 23 based. Other values are listed in ``pyqubes.constants``
        '''
        self.name = pyqubes.validate.linux_hostname(name)
        self.operating_system = operating_system
        self.enact_function = pyqubes.enact.call if proactive else pyqubes.enact.echo
        self.internet = InternetConnection(self)
    
    def enact(self, args):
        '''
        Enact a list of command arguments using the VM's ``enact_function``

        Any one of the functions in ``pyqubes.qubes``,``pyqubes.qubesdb``
        or ``pyqubes.qvm`` will return arguments in the correct format.
        '''
        return self.enact_function(args)

    def run(self, command, **kwargs):
        command = "'{0}'".format(command)
        kwargs.update({
            'pass_io': True
        })
        return self.enact(pyqubes.qvm.qvm_run(self.name, command, **kwargs))

    def shutdown(self, **kwargs):
        '''
        Shutdown the VM
        '''
        return self.enact(pyqubes.qvm.qvm_shutdown(self.name, wait=True, **kwargs))

    def start(self, **kwargs):
        '''
        Start the VM
        '''
        return self.enact(pyqubes.qvm.qvm_start(self.name, **kwargs))

    def firewall(self, **kwargs):
        '''
        Edit the VM firewall
        '''
        return self.enact(pyqubes.qvm.qvm_firewall(self.name, **kwargs))

    def internet_online(self):
        '''
        Can be explicity called to open the VM firewall to 'allow'.

        In most cases you should use``with vm.internet``::

            vm = TemplateVM('foo')
            vm.start()
            # Templates are offline be default
            with vm.internet as inet:
                # Template now has unrestricted internet access
                vm.update()
            # Firewall is restored automatically
        
        '''
        return self.enact(pyqubes.qvm.qvm_firewall(self.name, set_policy='allow'))

    def internet_offline(self):
        '''
        Can be explicity called to close the VM firewall to 'deny'.
        '''
        return self.enact(pyqubes.qvm.qvm_firewall(self.name, set_policy='deny'))

# TODO: Could TemplateVM and AppVM have metaclassed magic methods?
class TemplateVM(VM):
    def __init__(self, *args, **kwargs):
        super(TemplateVM, self).__init__(*args, **kwargs)

    def update(self):
        '''
        Smartly runs the relevant package manager updates for the TemplateVM
        '''
        if self.operating_system in pyqubes.constants.FEDORA_ALL:
            update_command = "sudo dnf check-update && sudo dnf -y upgrade"
        elif self.operating_system in pyqubes.constants.DEBIAN_ALL:
            update_command = "sudo apt-get update && sudo apt-get -y upgrade"
        else:
            raise ValueError("Could not update TemplateVM '{0}': Unknown OS '{1}'".format(self.name, self.operating_system))
        return self.run(update_command)
    
class AppVM(VM):
    def __init__(self, *args, **kwargs):
        super(AppVM, self).__init__(*args, **kwargs)

