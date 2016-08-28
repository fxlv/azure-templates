#!/usr/bin/env python
import ipdb
import os
from azurepy import vm

if os.path.exists("account.py"):
    import account
    subscription_id = account.subscription_id

vm_name = "winstar"
a = vm.AzureVM(subscription_id)
a.set_vm("winstar")
if a.is_running():
    print "Stopping ..."
    a.deallocate_vm()
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
