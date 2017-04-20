#!/usr/bin/env python
'''
Utility functions for pyqubes

Utilities have no dependencies.
'''

import logging

def object_fullname(obj):
    '''Returns the full absolute name of the object provided'''
    fullname = obj.__module__ + "." + obj.__class__.__name__
    return fullname

def object_logger(obj):
    '''
    Returns a correctly named logger for the given object.
    
    Call as self.logger = object_logger(self)
    '''
    fullname = object_fullname(obj)
    logger = logging.getLogger(fullname)
    return logger

