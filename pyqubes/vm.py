
import pyqubes.constants
import pyqubes.enact
import pyqubes.qvm
import pyqubes.validate


class VM(object):
    def __init__(self, name, proactive=False, operating_system=pyqubes.constants.FEDORA_23):
        self.name = pyqubes.validate.linux_hostname(name)
        self.operating_system = operating_system
        self.enact_function = pyqubes.enact.call if proactive else pyqubes.enact.echo
    
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
        return self.enact(pyqubes.qvm.qvm_shutdown(self.name, wait=True, **kwargs))

# TODO: Could TemplateVM and AppVM have metaclassed magic methods?
class TemplateVM(VM):
    def __init__(self, *args, **kwargs):
        super(TemplateVM, self).__init__(*args, **kwargs)

    def update(self):
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

