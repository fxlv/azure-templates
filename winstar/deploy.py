#!/usr/bin/env python
import os
from azurepy import vm

if os.path.exists("account.py"):
    import account
    subscription_id = account.subscription_id

vm_name = "winstar"
a = vm.AzureVM(subscription_id)
a.set_vm("winstar")
