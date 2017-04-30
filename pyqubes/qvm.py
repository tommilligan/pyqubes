import pyqubes.compile
import pyqubes.utils
import pyqubes.validate

def qvm_run(vm_name,
            command,
            quiet=False,
            auto=False,
            user='',
            tray=False,
            all_vms=False,
            exclude=[],
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
    command_args = ["qvm-run", pyqubes.validate.linux_hostname(vm_name), command]
    command_args.extend(pyqubes.compile.flags_boolean({
        '--quiet': quiet,
        '--auto': auto,
        '--tray': tray,
        '--all': all_vms,
        '--wait': wait,
        '--shutdown': shutdown,
        '--pause': pause,
        '--unpause': unpause,
        '--pass-io': pass_io,
        '--force': force
    }))
    command_args.extend(pyqubes.compile.flags_store({
        '--user': pyqubes.validate.linux_username(user) if user else None,
        '--localcmd': localcmd
    }))
    [command_args.extend(pyqubes.compile.flags_store({
        '--exclude': pyqubes.validate.linux_hostname(exclude_single) if exclude_single else None
    })) for exclude_single in exclude]
    return command_args

def qvm_shutdown(vm_name,
            quiet=False,
            force=False,
            wait=False,
            all_vms=False,
            exclude=[]):
    '''
    qvm-shutdown
    '''
    command_args = ["qvm-shutdown", pyqubes.validate.linux_hostname(vm_name)]
    command_args.extend(pyqubes.compile.flags_boolean({
        '--quiet': quiet,
        '--force': force,
        '--wait': wait,
        '--all': all_vms
    }))
    [command_args.extend(pyqubes.compile.flags_store({
        '--exclude': pyqubes.validate.linux_hostname(exclude_single) if exclude_single else None
    })) for exclude_single in exclude]
    return command_args

def qvm_firewall(vm_name,
            list_view=False,
            add_rule='',
            del_rule='',
            set_policy='',
            set_icmp='',
            set_dns='',
            set_yum_proxy='',
            numeric=False):
    '''
    qvm-firewall
    '''
    command_args = ["qvm-firewall", pyqubes.validate.linux_hostname(vm_name)]
    command_args.extend(pyqubes.compile.flags_boolean({
        '--list': list_view,
        '--numeric': numeric
    }))
    command_args.extend(pyqubes.compile.flags_store({
        '--add': add_rule,
        '--del': del_rule,
        '--policy': pyqubes.validate.firewall_policy(set_policy) if set_policy else None,
        '--icmp': pyqubes.validate.firewall_policy(set_icmp) if set_icmp else None,
        '--dns': pyqubes.validate.firewall_policy(set_dns) if set_dns else None,
        '--yum_proxy': pyqubes.validate.firewall_policy(set_yum_proxy) if set_yum_proxy else None
    }))
    return command_args

def qvm_start(vm_name,
            quiet=False,
            no_guid=False,
            console=False,
            dvm=False,
            custom_config=''):
    '''
    qvm-start
    '''
    command_args = ["qvm-start", pyqubes.validate.linux_hostname(vm_name)]
    command_args.extend(pyqubes.compile.flags_boolean({
        '--quiet': quiet,
        '--no-guid': no_guid,
        '--console': console,
        '--dvm': dvm
    }))
    command_args.extend(pyqubes.compile.flags_store({
        '--custom-config': custom_config
    }))
    return command_args

def qvm_clone(vm_name,
            clone_name,
            quiet=False,
            path=''):
    '''
    qvm-clone
    '''
    command_args = ["qvm-clone", pyqubes.validate.linux_hostname(vm_name), pyqubes.validate.linux_hostname(clone_name)]
    command_args.extend(pyqubes.compile.flags_boolean({
        '--quiet': quiet
    }))
    command_args.extend(pyqubes.compile.flags_store({
        '--path': path
    }))
    return command_args

def qvm_create(vm_name,
            template='',
            label='',
            proxy=False,
            net=False,
            hvm=False,
            hvm_template=False,
            root_move_from='',
            root_copy_from='',
            standalone=False,
            mem=0,
            vcpus=0,
            internal=False,
            force_root=False,
            quiet=False):
    '''
    qvm-create
    '''
    command_args = ["qvm-create", pyqubes.validate.linux_hostname(vm_name)]
    command_args.extend(pyqubes.compile.flags_boolean({
        '--proxy': proxy,
        '--net': net,
        '--hvm': hvm,
        '--hvm_template': hvm_template,
        '--standalone': standalone,
        '--internal': internal,
        '--force-root': force_root,
        '--quiet': quiet
    }))
    command_args.extend(pyqubes.compile.flags_store({
        '--template': pyqubes.validate.linux_hostname(template) if template else None,
        '--label': pyqubes.validate.label_color(label) if label else None,
        '--root-move-from': root_move_from,
        '--root-copy-from': root_copy_from,
        '--mem': mem,
        '--vcpus': vcpus
    }))
    return command_args

def qvm_remove(vm_name,
            quiet=False,
            just_db=False,
            force_root=False):
    '''
    qvm-remove
    '''
    command_args = ["qvm-remove", pyqubes.validate.linux_hostname(vm_name)]
    command_args.extend(pyqubes.compile.flags_boolean({
        '--quiet': quiet,
        '--just-db': just_db,
        '--force-root': force_root
    }))
    return command_args

