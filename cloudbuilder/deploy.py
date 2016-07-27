#!/usr/bin/env python
import os
import sys
from subprocess import Popen, PIPE
import json



subscriptionId="lalala-lalala-lalala"
vmName="cloudhawkbuild"
resourceGroupLocation="northeurope"

deploymentName="${vmName}_deployment"
resourceGroupName="${vmName}_rg"
templateFilePath="template.json"
parametersFilePath="parameters.json"

# first check what vms already exist
class AzureVM():
    def __init__(self, subscriptionId):
        self.subscriptionId = subscriptionId
        if not self.check_subscription():
            print "Invalid subscription provided"
            sys.exit(1)

    def run_command(self, command):
        process = Popen(command.split(), stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print "Stderr: {}".format(stderr)
        return json.loads(stdout)

    def check_subscription(self):
        """Return True if the provided subscriptionId is valid."""
        accounts = self.get_accounts()
        for account in accounts:
            if account["id"] == self.subscriptionId:
                return True
        return False


    def get_accounts(self):
        return self.run_command("azure account list --json")


    def list(self):
        print self.run_command("azure vm list --json")


a = AzureVM(subscriptionId)
a.list()

#azure account set $subscriptionId
#
#
#if [ -z "$resourceGroupLocation" ] ; 
#then
#	echo "Using existing resource group..."
#else 
#	echo "Creating a new resource group..." 
#	azure group create --name $resourceGroupName --location $resourceGroupLocation
#fi
#
#
#echo "Starting deployment..."
#azure group deployment create  --name $deploymentName --resource-group $resourceGroupName --template-file $templateFilePath --parameters-file $parametersFilePath
