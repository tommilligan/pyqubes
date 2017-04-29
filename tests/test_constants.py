#!/usr/bin/env python

import unittest

import six

import pyqubes.constants as c


class TestConstants(unittest.TestCase):
    def test_constants_fedora_all(self):
        six.assertCountEqual(self, c.FEDORA_ALL, [c.FEDORA, c.FEDORA_23])
    
    def test_constants_debian_all(self):
        six.assertCountEqual(self, c.DEBIAN_ALL, [c.DEBIAN, c.DEBIAN_8])
    
