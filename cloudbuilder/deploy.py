#!/usr/bin/env python
import os
import sys
from subprocess import Popen, PIPE
import json
import vm


if os.path.exists("account.py"):
    import account
    subscription_id = account.subscription_id

vm_name="cloudhawkbuild"
resource_group_location="northeurope"

deployment_name="{}deployment".format(vm_name)
resource_group_name="lalala3"
template_file_path="template.json"
parameters_file_path="parameters.json"


# first check what vms already exist
# the flow goes like this:
# * create AzureVM object
# * create VM
# ** check if subscription id is provided and check if it's valid, 
#    set it as the default
# ** check if resource group already exists, create it if it doesn't
# ** create the VM

a = vm.AzureVM(subscription_id)
a.create_vm(deployment_name, resource_group_name, resource_group_location, template_file_path, parameters_file_path)
a.list()

#a.create_vm(name="lalaal1", resource_group="lalala1_group", template_file="lalala", parameters_file="lalala")
