#!/usr/bin/env python
from azurepy import vm, account
import sys

a = vm.AzureVM(account.get_subscription_id())
if not a.set_vm("winstar"):
    print "This VM is not available"
    print "You'll have to re-deploy"
    sys.exit(1)

if a.is_running():
    print "VM is running"
    print "IP: {}".format(a.get_ip())
else:
    print "VM is not running: {}".format(a.get_power_state())
