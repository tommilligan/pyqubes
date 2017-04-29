
import pyqubes.enact
import pyqubes.qvm
import pyqubes.validate


class VM(object):
    def __init__(self, name, proactive=False):
        self.name = pyqubes.validate.linux_hostname(name)
        self.enact_function = pyqubes.enact.call if proactive else pyqubes.enact.echo
    
    def enact(self, args):
        '''
        Enact a list of command arguments using the VM's ``enact_function``
        '''
        return self.enact_function(args)

    def shutdown(self, **kwargs):
        return self.enact(pyqubes.qvm.qvm_shutdown(self.name, **kwargs))

# TODO: Could TemplateVM and AppVM have metaclassed magic methods?
class TemplateVM(VM):
    def __init__(self, *args, **kwargs):
        super(TemplateVM, self).__init__(*args, **kwargs)


class AppVM(VM):
    def __init__(self, *args, **kwargs):
        super(AppVM, self).__init__(*args, **kwargs)

