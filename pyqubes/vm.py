#!/usr/bin/env python
'''
Python objects representing QubesOS objects
'''

import pyqubes.constants
import pyqubes.enact
import pyqubes.qvm
import pyqubes.validate


class VMMagicFirewall(object):
    '''
    Helper class for opening and closing the VM fireall automatically
    
    :param vm: A ``VM`` instance.
    '''
    def __init__(self, vm):
        self.vm = vm

    def __enter__(self):
        self.vm.firewall_open()

    def __exit__(self, type, value, traceback):
        self.vm.firewall_close()

class VMMagicAnimate(object):
    '''
    Helper class for starting and shutting down the VM automatically
    
    :param vm: A ``VM`` instance.
    '''
    def __init__(self, vm):
        self.vm = vm

    def __enter__(self):
        self.vm.start()

    def __exit__(self, type, value, traceback):
        self.vm.shutdown()

class VM(object):
    '''
    The VM object represants a QubesOS VM. Its methods are common accross
    both AppVMs and TemplateVMs.

    VM should not be instanciated directly - use TemplateVM or AppVM.

    By default, all VMs are Fedora 23 based. Other values are listed in ``pyqubes.constants``
    '''
    def __init__(self, name, proactive=False, operating_system=pyqubes.constants.FEDORA_23):
        self.name = pyqubes.validate.linux_hostname(name)
        self.proactive = proactive
        self.operating_system = operating_system
        
        self.enact_function = pyqubes.enact.call if proactive else pyqubes.enact.echo
        
        self.animate = VMMagicAnimate(self)
        self.internet = VMMagicFirewall(self)
    
    def enact(self, args):
        '''
        Enact a list of command arguments using the VM's ``enact_function``

        Any one of the functions in ``pyqubes.qubes``,``pyqubes.qubesdb``
        or ``pyqubes.qvm`` will return arguments in the correct format.
        '''
        return self.enact_function(args)

    def info(self, info):
        '''
        Echo information from pyqubes using the VM's enact method
        '''
        info = '{0}|{1}'.format(self.name, info)
        return self.enact(pyqubes.compile.info(info))

    # Direct command bindings

    def run(self, command, quote=True, **kwargs):
        '''
        Run a command on the VM.

        Please note:
        * ``--pass-io`` is always set, to run commands synchronously
        * Commands are automatically encapsulated in single quotes::

            vm = TemplateVM('spam')
            vm.run('echo "foo bar"')
            # produces: qvm-run spam 'echo "foo bar"'
        
        :param bool quote: By default command is single quoted - set ``False`` to disable
        '''
        if quote:
            command = "'{0}'".format(command)
        kwargs.update({
            'pass_io': True
        })
        self.info('Running command {0}'.format(command))
        return self.enact(pyqubes.qvm.qvm_run(self.name, command, **kwargs))

    def shutdown(self, **kwargs):
        '''
        Shutdown the 
        
        Please note:
        * ``--wait`` is always set, to run commands synchronously
        '''
        kwargs.update({
            'wait': True
        })
        self.info('Shutting down')
        return self.enact(pyqubes.qvm.qvm_shutdown(self.name, **kwargs))

    def start(self, **kwargs):
        '''
        Start the VM explicitly.

        In most cases you should use``with vm.animate``::

            vm = TemplateVM('foo')
            # Template is not started on instanciation
            with vm.animate:
                # Template is now running
                vm.update()
            # VM is shut down automatically
        
        '''
        self.info('Starting')
        return self.enact(pyqubes.qvm.qvm_start(self.name, **kwargs))

    def firewall(self, **kwargs):
        '''
        Edit the VM firewall
        '''
        self.info('Adjusting firewall')
        return self.enact(pyqubes.qvm.qvm_firewall(self.name, **kwargs))

    def remove(self, **kwargs):
        '''
        Remove the VM
        '''
        self.info('Removing')
        return self.enact(pyqubes.qvm.qvm_remove(self.name, **kwargs))

    # Helper functions

    def firewall_open(self):
        '''
        Can be explicity called to open the VM firewall to 'allow'.

        In most cases you should use``with vm.internet``::

            vm = TemplateVM('foo')
            with vm.animate:
                # Templates are offline be default
                with vm.internet:
                    # Template now has unrestricted internet access
                    vm.run('curl http://ipecho.net/plain')
                # Firewall is restored automatically
                # This will now fail
                vm.run('curl http://ipecho.net/plain')
        
        '''
        self.info('Opening firewall')
        return self.enact(pyqubes.qvm.qvm_firewall(self.name, set_policy='allow'))

    def firewall_close(self):
        '''
        Can be explicity called to close the VM firewall to 'deny'.
        '''
        self.info('Closing firewall')
        return self.enact(pyqubes.qvm.qvm_firewall(self.name, set_policy='deny'))

# TODO: Could TemplateVM and AppVM have metaclassed magic methods?
class TemplateVM(VM):
    '''
    TemplateVM - for installing apps
    '''
    def __init__(self, *args, **kwargs):
        super(TemplateVM, self).__init__(*args, **kwargs)

    def clone(self, clone_name, **kwargs):
        '''
        Clone the TemplateVM and return a new TemplateVM

        :param string clone_name: Name of the new VM
        :returns: The new ``TemplateVM`` instance
        '''
        self.info('Cloning to \'{0}\''.format(clone_name))
        self.enact(pyqubes.qvm.qvm_clone(self.name, clone_name, **kwargs))
        return TemplateVM(clone_name, proactive=self.proactive, operating_system=self.operating_system)

    def create_app(self, app_name, **kwargs):
        '''
        Create and return a new AppVM based on the TemplateVM.
        
        Please note:
        * If ``label`` is not set, it will default to ``red``

        :param string app_name: Name of the new VM
        :returns: The new ``AppVM`` instance
        '''
        kwargs.update({
            'template': self.name,
            'label': kwargs['label'] if kwargs.get('label', None) else pyqubes.constants.RED
        })
        self.info('Creating app \'{0}\''.format(app_name))
        self.enact(pyqubes.qvm.qvm_create(app_name, **kwargs))
        return AppVM(app_name, proactive=self.proactive, operating_system=self.operating_system)
    
    def update(self):
        '''
        Smartly runs the relevant package manager updates for the TemplateVM
        '''
        if self.operating_system in pyqubes.constants.FEDORA_ALL:
            update_command = "sudo dnf -y upgrade --refresh"
        elif self.operating_system in pyqubes.constants.DEBIAN_ALL:
            update_command = "sudo apt-get update && sudo apt-get -y dist-upgrade"
        else:
            raise ValueError("Could not update TemplateVM '{0}': Unknown OS '{1}'".format(self.name, self.operating_system))
        self.info('Updating')
        return self.run(update_command)
    
class AppVM(VM):
    '''
    AppVM - for running apps
    '''
    def __init__(self, *args, **kwargs):
        super(AppVM, self).__init__(*args, **kwargs)

