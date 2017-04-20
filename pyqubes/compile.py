import six

def flags_boolean(flags):
    '''
    Return a list of string values, corresponding to the given keys whose values evaluate to True
    
    :param dict flags: A dictionary in the form ``{'--flag': boolean}``, where ``boolean`` is used
            to determine whether ``--flag`` is included in the output.
    '''
    flags_true = [k for k, v in six.iteritems(flags) if v]
    return flags_true