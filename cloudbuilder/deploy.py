#!/usr/bin/env python
import os
from azurepy import vm

if os.path.exists("account.py"):
    import account
    subscription_id = account.subscription_id

vm_name = "cloudhawkbuild"
resource_group_location = "northeurope"

deployment_name = "{}deployment".format(vm_name)
resource_group_name = "lalala3"
template_file_path = "template.json"
parameters_file_path = "parameters.json"

a = vm.AzureVM(subscription_id)
a.create_vm(deployment_name, resource_group_name, resource_group_location,
            template_file_path, parameters_file_path)
a.list()
