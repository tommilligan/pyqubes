#! /usr/bin/env python
'''
The ``compile`` module converts instructions from pythonic data structures
into flat lists.abs

These may require further processing before being passed to the
``enact`` module for action.
'''
import six

from pyqubes.utils import flatten_list


def flags_boolean(flags):
    '''
    Return a list of string values, corresponding to the given keys whose values evaluate to True

    All keys and values will be converted to strings.

    :param dict flags: A dictionary in the form ``{'--flag': boolean}``, where ``boolean`` is used
            to determine whether ``--flag`` is included in the output.
    :returns: A flat list of strings
    '''
    flags_list = [str(k) for k, v in six.iteritems(flags) if v]
    return flags_list

def flags_store(flags):
    '''
    Return a list of string values, corresponding to the given keys and values whose values evaluate to True
    
    The output is a flat list of all strings.
    
    All keys and values will be converted to strings.

    :param dict flags: A dictionary in the form ``{'--flag': value}``, where ``value`` is used
            to determine whether the entry is included in the output.
    :returns: A flat list of strings
    '''
    flags_nested = [[str(k), str(v)] for k, v in six.iteritems(flags) if v]
    flags_list = flatten_list(flags_nested)
    return flags_list

def flags_store_iterable(flags):
    '''
    Calls ``flags_store`` for each value within each key in ``flags``.

    e.g. {'--fruits': ['apple', 'pear']} results in ['--fruits', 'apple', '--fruits', 'pear']

    :param dict flags: A dictionary in the form ``{'--flag': value}``, where ``value`` is an iterable.
    :returns: A flat list of strings
    :raises: ``TypeError`` if values are not iterable
    '''
    flags_nested = [[[str(k), str(single_value)] for single_value in v] for k, v in six.iteritems(flags) if v and len(v) > 0]
    flags_list = flatten_list(flatten_list(flags_nested))
    return flags_list

def info(info, quote=True, style=True):
    '''
    Returns the given string ``info`` as a set of echo arguments.

    Optionally provides quoting and terminal styling.

    :param string info: Info string to add to script
    :param bool quote: By default quote given sting in single quotes
    :param bool style: By default add 
    :returns: A flat list of strings
    '''
    info = 'pyqubes|{0}'.format(info)
    if style:
        info = '\e[36m{0}\e[39m'.format(info)
    if quote:
        info = '\'{0}\''.format(info)
    return ['echo', '-e', info]

