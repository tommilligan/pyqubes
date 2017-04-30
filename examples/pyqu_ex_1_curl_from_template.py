#! /usr/bin/env python
'''
Use pyqubes to clone a new TemplateVM and install Google Chrome
'''
from pyqubes.vm import TemplateVM

internet_test_command = 'curl http://ipecho.net/plain'

# Create a pyqubes TemplateVM representing the existing QubesOS TemplateVM
vm_vanilla = TemplateVM('fedora-23')
# Create a new AppVM
example_app = vm_vanilla.create_app('example-app-pyqu-ex-1')

# Start the AppVM
with example_app.animate:
    # AppVMs have an open firewall by default
    example_app.run(internet_test_command)
example_app.remove()

# Start the TemplateVM
with vm_vanilla.animate:
    # To the same in a template, open the firewall temporarily
    with vm_vanilla.internet:
        vm_vanilla.run(internet_test_command)
    # It will be closed automatically
    vm_vanilla.run(internet_test_command)

