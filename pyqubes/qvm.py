import pyqubes.compile
import pyqubes.utils
import pyqubes.validate

def qvm_run(command,
            quiet=False,
            auto=False,
            user='',
            tray=False,
            all=False,
            exclude=[], # turn into repeated kwargs
            wait=False,
            shutdown=False,
            pause=False,
            unpause=False,
            pass_io=False,
            localcmd='',
            force=False):
    '''
    qvm-run
    '''
    command_args = ["qvm-run", command]
    command_args.extend(pyqubes.compile.flags_boolean({
        '--quiet': quiet,
        '--auto': auto,
        '--tray': tray,
        '--all': all,
        '--wait': wait,
        '--shutdown': shutdown,
        '--pause': pause,
        '--unpause': unpause,
        '--pass-io': pass_io,
        '--force': force
    }))
    if pyqubes.validate.linux_username(user):
        command_args.extend(['--user', user])
    return command_args