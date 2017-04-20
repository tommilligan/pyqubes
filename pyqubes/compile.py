import six

from pyqubes.utils import flatten_list


def flags_boolean(flags):
    '''
    Return a list of string values, corresponding to the given keys whose values evaluate to True

    All keys and values will be converted to strings.

    :param dict flags: A dictionary in the form ``{'--flag': boolean}``, where ``boolean`` is used
            to determine whether ``--flag`` is included in the output.
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
    '''
    flags_nested = [[str(k), str(v)] for k, v in six.iteritems(flags) if v]
    flags_list = flatten_list(flags_nested)
    return flags_list

def flags_store_iterable(flags):
    '''
    Calls ``flags_store`` for each value within each key in ``flags``.

    e.g. {'--fruits': ['apple', 'pear']} results in ['--fruits', 'apple', '--fruits', 'pear']

    :param dict flags: A dictionary in the form ``{'--flag': value}``, where ``value`` is an iterable.
    :raises: TypeError if values are not iterable
    '''
    flags_nested = [[[str(k), str(single_value)] for single_value in v] for k, v in six.iteritems(flags) if v and len(v) > 0]
    flags_list = flatten_list(flatten_list(flags_nested))
    return flags_list

    