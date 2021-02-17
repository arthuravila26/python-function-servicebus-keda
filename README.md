# Azure Functions and Keda using ServiceBus queues

A simple Python Azure Functions sample that autoscaling automatically when an event arrives 
in a queue on Azure ServiceBus using [Keda](https://keda.sh) and deploying on AKS.
This samples has as base the sample made by [tomconte](https://github.com/tomconte/sample-keda-queue-jobs).

## Pre-requisites

- [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools)
- [Azure Subscription](https://azure.microsoft.com/en-us/free/search/?&ef_id=Cj0KCQiA962BBhCzARIsAIpWEL0yJq5fIWttHFgLd9uGDa60_uvpeIwIKkM0Yp7tPV2X5MO-vgYe1IkaAmDjEALw_wcB:G:s&OCID=AID2100014_SEM_Cj0KCQiA962BBhCzARIsAIpWEL0yJq5fIWttHFgLd9uGDa60_uvpeIwIKkM0Yp7tPV2X5MO-vgYe1IkaAmDjEALw_wcB:G:s&dclid=CjgKEAiA962BBhDLtsGQrbzDjhgSJAAz72xRYG7Mk8H3qy1-MUwv68CQOOMrp4__0iXetkmGBVFayPD_BwE) to create an AKS and an Azure ServiceBus. You can use a free-trial for it.
- [Docker](https://docs.docker.com/get-docker/) and a [DockerHub](https://hub.docker.com) account.
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Python 3.x](https://www.python.org/downloads/)

## Setup

From here I will assume that you already have an AKS cluster created with [Keda 2.1](https://keda.sh/docs/2.1/deploy/) installed, a ServiceBus with a queue and connection string.
This setup I gonna show how you can run from here sooner I you write an article with a tutorial from zero to hero from this tutorial. I you drop it here as soon as I finish it.

### 1. Clone the project
```
git clone https://github.com/arthuravila26/python-function-servicebus-keda.git
cd python-function-servicebus-keda
```
