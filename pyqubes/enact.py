import subprocess
import sys

import six


def echo(args, file=None):
    '''
    Echo a list of arguments (as given to ``subprocess.call``) to the given stream.

    This defaults to ``stdout``, but can be changed to any stream-like object such as a file handle.

    :param args: A string or list of strings
    :param file: A file-like object to stream output to. Defaults to ``sys.stdout``
    '''
    if file is None:
        file = sys.stdout

    if isinstance(args, six.string_types + (six.text_type,)):
        args = [args]
    
    six.print_(*args, file=file, flush=True)

def call(args):
    '''
    Thin wrapper for builtin subprocess.call
    '''
    return subprocess.check_call(args)
