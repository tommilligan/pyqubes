#! /usr/bin/env python

from pyqubes.vm import TemplateVM

vm_vanilla = TemplateVM('fedora-23')
with vm_vanilla.supervise:
    with mv_vanilla.internet:
