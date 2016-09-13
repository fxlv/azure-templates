#!/usr/bin/env python
from azurepy import vm, account

subscription_id = account.get_subscription_id()

vm_name = "winstar"
a = vm.AzureVM(subscription_id)
if a.set_vm("winstar"):
    print "This VM is already deployed"
    if a.is_running():
        print "And it is running..."
    else:
        print "VM not running, will start it up"
        a.start_vm()
        a.set_vm("winstar")  # update status
        print a.get_power_state()
        if a.is_running():
            print "VM is running"
            print "IP: {}".format(a.get_ip())
        else:
            print "VM failed to start"
else:
    # vm not available, try to deploy
    resource_group_location = "northeurope"

    deployment_name = "{}deployment".format(vm_name)
    resource_group_name = "lalala5"
    template_file_path = "template.json"
    parameters_file_path = "parameters.json"

    a = vm.AzureVM(subscription_id)
    a.create_vm(deployment_name, resource_group_name, resource_group_location,
                template_file_path, parameters_file_path)
    a.list()
