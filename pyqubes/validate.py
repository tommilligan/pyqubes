import re


def linux_username(username):
    '''
    Linux usernames are recommended to match [a-z_][a-z0-9_-]*[$]

    :param string username: Username to check
    :rtype bool:
    '''
    okay_pattern = True if re.match(r'^[a-z_][a-z0-9_-]*\$?$', username) else False
    okay_length = len(username) <= 32 and len(username) >= 0
    valid_username = okay_length and okay_pattern
    return valid_username