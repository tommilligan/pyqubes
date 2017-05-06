# pyqubes

[![PyPI](https://img.shields.io/pypi/v/pyqubes.svg)](https://pypi.python.org/pypi/pyqubes)
[![PyPI](https://img.shields.io/pypi/pyversions/pyqubes.svg)](https://pypi.python.org/pypi/pyqubes)
[![Documentation Status](https://readthedocs.org/projects/pyqubes/badge/?version=master)](http://pyqubes.readthedocs.io/en/master/?badge=master)
[![license](https://img.shields.io/github/license/tommilligan/pyqubes.svg)](https://pypi.python.org/pypi/pyqubes)

[![Travis branch](https://img.shields.io/travis/tommilligan/pyqubes/develop.svg)](https://travis-ci.org/tommilligan/pyqubes)
[![codecov](https://codecov.io/gh/tommilligan/pyqubes/branch/develop/graph/badge.svg)](https://codecov.io/gh/tommilligan/pyqubes/branch/develop)
[![Requirements Status](https://requires.io/github/tommilligan/pyqubes/requirements.svg?branch=develop)](https://requires.io/github/tommilligan/pyqubes/requirements/?branch=develop)

**pyqubes** aims to make the automation of dom0 tasks in QubesOS easier to document and share. Nothing additional needs to be installed in dom0 - pyqubes generates plain bash scripts dom0 can understand, with the heavy lifting done on an AppVM.

```python
from pyqubes.vm import TemplateVM
vm = TemplateVM('fedora-23')
with vm.animate:
    vm.update()
    with vm.internet:
        vm.run('curl http://ipecho.net/plain')
```
generates the equialent bash script
```bash
qvm-start fedora-23
qvm-run fedora-23 'sudo dnf -y upgrade --refresh' --pass-io
qvm-firewall fedora-23 --policy allow
qvm-run fedora-23 'curl http://ipecho.net/plain' --pass-io
qvm-firewall fedora-23 --policy deny
qvm-shutdown fedora-23 --wait
```

## Installation

Install on an AppVM using pip:
```bash
pip install pyqubes
```

## Use

### Generating scripts

There are a few example python scripts available to download.

Running a python script transcribes a matching bash script to `stdout`.
```bash
python pyqubes_script.py > qubes_script.sh
```

### Running scripts

#### **Warning**
--------------------
**The entire point of this project is to run semi-arbitrary code via dom0** 
If you're a QubesOS user, this probably goes against everything you stand for.

This project is not meant for everyday use. It is meant for:
* documenting your QubesOS installation in a pythonic format
* automating setup of TemplateVMs and AppVMs
* sharing recipes of good QubesOS setups

If you're still interested, read on...

--------------------
Bash scripts from an AppVM can be run from `dom0` using the following:
```bash
bash <(qvm-run --pass-io <AppVM_name> 'cat ~/path/to/bash/script.sh')
```
or, to run the python script directly:
```bash
bash <(qvm-run --pass-io <AppVM_name> 'python ~/path/to/python/script.py')
```

Output will be color-coded as:

|color|source|
|---|---|
|white|dom0|
|red|TemplateVM/AppVM|
|blue|pyqubes|

### As a wrapper

**pyqubes** can also be used a simple wrapper library, although it's not reccommended:
```python
import subprocess
from pyqubes.qvm import qvm_start
subprocess.call(qvm_start('fedora-23', quiet=True))
```


## Documentation

The full documentation is available [here on readthedocs](http://pyqubes.readthedocs.io/en/master/)

## Development

Pull Requests and issues are always welcome.

Clone the repo and install with development requirements using pip:
```bash
git clone https://github.com/tommilligan/pyqubes
cd pyqubes
pip install .[dev]
```

Please ensure you add matching tests for your commits!
```bash
nose2 --with-coverage
```

