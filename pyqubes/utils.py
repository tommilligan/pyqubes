#!/usr/bin/env python
'''
Utility functions for pyqubes

Utilities have no dependencies.
'''

import logging
import re

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

def validate_linux_username(username):
    '''
    Linux usernames are recommended to match [a-z_][a-z0-9_-]*[$]

    :param string username: Username to check
    :rtype bool:
    '''
    okay_pattern = True if re.match(r'^[a-z_][a-z0-9_-]*\$?$', username) else False
    okay_length = len(username) <= 32 and len(username) >= 0
    valid_username = okay_length and okay_pattern
    return valid_username