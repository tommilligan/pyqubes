import re

# TODO replace with config (regex, lambda, error message)
def linux_username(username):
    '''
    Linux usernames are recommended to match ``^[a-z_][a-z0-9_-]*\$?$``

    :param string username: Username to check
    :returns: ``username`` if valid, else ``ValueError``
    '''
    okay_pattern = True if re.match(r'^[a-z_][a-z0-9_-]*\$?$', username) else False
    okay_length = len(username) <= 32 and len(username) >= 0
    valid_username = okay_length and okay_pattern
    if not valid_username:
        raise ValueError('Invalid linux username: {0}'.format(username))
    else:
        return username

def linux_hostname(hostname):
    '''
    Linux hostnames are recommended to match ``^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$``

    :param string hostname: Hostname to check
    :returns: ``hostname`` if valid, else ``ValueError``
    '''
    okay_pattern = True if re.match(r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$', hostname) else False
    okay_length = len(hostname) <= 253 and len(hostname) >= 0
    valid_hostname = okay_length and okay_pattern
    if not valid_hostname:
        raise ValueError('Invalid linux hostname: {0}'.format(hostname))
    else:
        return hostname

def firewall_policy(policy):
    '''
    qvm-firewall policy string should match ``^(allow|deny)$``

    :param string policy: Policy string to check
    :returns: ``policy`` if valid, else ``ValueError``
    '''
    if policy not in ["allow", "deny"]:
        raise ValueError('Invalid qvm-firewall policy: {0}'.format(policy))
    else:
        return policy

