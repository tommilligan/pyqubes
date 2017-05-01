#! /usr/bin/env python
'''
Say Hello World1! from a temporary AppVM
'''
from pyqubes.vm import TemplateVM

# Create a pyqubes TemplateVM representing the existing QubesOS TemplateVM
vm_vanilla = TemplateVM('fedora-23')

# Create a new temporary AppVM
example_app = vm_vanilla.create_app('example-app-pyqu-ex-2')
# Start the AppVM
with example_app.animate:
    # Say Hello World!
    example_app.run('echo "Hello World!"')
# Remove the temporary AppVM
example_app.remove()

