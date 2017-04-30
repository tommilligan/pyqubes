
Pythonic Classes
================

VM
--

The top level ``VM`` object holds common methods for VMs.

It should not be instanciated directly - use  the
lower level ``TemplateVM`` and ``AppVM`` objects instead.

.. autoclass:: pyqubes.vm.VM
   :members:


TeamplateVM & AppVM
-------------------

These represent the actual VMs within QubesOS.

Methods mentioned here are specific to the VM type.

.. autoclass:: pyqubes.vm.TemplateVM
   :members:

.. autoclass:: pyqubes.vm.AppVM
   :members:


Helper Classes
--------------

.. autoclass:: pyqubes.vm.InternetConnection
   :members:

