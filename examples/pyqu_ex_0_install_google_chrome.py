#! /usr/bin/env python
'''
Use pyqubes to clone a new TemplateVM and install Google Chrome
'''
from pyqubes.vm import TemplateVM

# Create a pyqubes TemplateVM representing the existing QubesOS TemplateVM
vm_vanilla = TemplateVM('fedora-23')
# Start the vm
with vm_vanilla.animate:
    # Ensure everything is up to date
    vm_vanilla.update()

# Clone a new VM to install third-party software in
vm_exotic = vm_vanilla.clone('fedora-23-pyqu-ex-0')
with vm_exotic.animate:
    # Add Google Chrome repo
    vm_exotic.run('echo -e "[google-chrome]\nname=google-chrome - \$basearch\nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch\nenabled=1\ngpgcheck=1\ngpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub" | sudo tee /etc/yum.repos.d/google-chrome.repo')
    # Install Google Chrome
    vm_exotic.run('sudo dnf -y install google-chrome-stable --refresh')
   

