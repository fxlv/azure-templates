#!/bin/bash

subscriptionId="yoursubscriptionidhere"
vmName="cloudhawkbuild"
resourceGroupLocation="northeurope"

deploymentName="${vmName}_deployment"
resourceGroupName="${vmName}_rg"
templateFilePath="template.json"
parametersFilePath="parameters.json"

azure account set $subscriptionId
if [ -z "$resourceGroupLocation" ] ; 
then
	echo "Using existing resource group..."
else 
	echo "Creating a new resource group..." 
	azure group create --name $resourceGroupName --location $resourceGroupLocation
fi


echo "Starting deployment..."
azure group deployment create  --name $deploymentName --resource-group $resourceGroupName --template-file $templateFilePath --parameters-file $parametersFilePath
