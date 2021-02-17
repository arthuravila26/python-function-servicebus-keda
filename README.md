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
This setup I gonna show how you can run from here. Bellow this setup area it's the tutorial that you can do from zero.

### 1. Clone the project
```
git clone https://github.com/arthuravila26/python-function-servicebus-keda.git
cd python-function-servicebus-keda
```
### 2. Insert SB connection string

In the file ```local.settings.json``` you must put the ServiceBus connection string at ```AzureWebJobsStorage```. This object will be use on ```functions.json``` as well.

### 3. Insert queue-name

In the file ```function.json``` you must include the queue name that your pod will listen and get up when an event arrives.
This queue name must be included in the ```scaledobject.yml```. This file is the configuration file that will set all you need to Keda.


### 4. Manifests

To deploy it in your cluster, you must modify the ```deployment.yml``` with yours configurations as pod name, namespace that this pod will run and whether you and to deploy this Dockerfile to your docker registry, you just need to change the image it will pull and the container name.

### 5. Deploying it with the pipeline

This pipeline has been made for deploy it in the easiest way as possible.
This pipeline will use my docker image in my docker registry, but you can easily change it and deploy your image in yours docker registry.
In the deploy stage, you just need to set up your environment in the pipeline. You can configure it in the Azure DevOps where you will run the pipeline.

### 6. Testing it

In the folder ```event-sender``` we have a python script that send events to your ServiceBus.
For run it you must export the ```AzureWebJobsStorage``` and the ```QUEUE_NAME``` to your environmentl like:
```
export AzureWebJobsStorage='<service-bus-connection>'
export QUEUE_NAME=<queue-name>
```

After that, you can set how many events you want to send in the ```method send_a_list_of_messages```.


## Tutorial

From here I will show you how you can create the function from zero and deploy it.
From this tutorial, you can use the manifests folder (with scaledobject.yml and deployment.yml) and the azure-pipelines.yml as well. This you
help you to deploy the function you created to your AKS cluster.

As I said in the setup, I will assume that you already have an AKS cluster with Keda 2.1 installed and a ServiceBus created as well.

### 1. Create a repository

You can start your project on Azure DevOps repos, GitHubs or GitLab. You just have to configure your Azure DevOps to connect in your repository for run the pipeline when you want to.
After create, clone your project to your machine.

### 2. Start a function

For create a new function you need do run:
```
func init . --docker
```
Running this command you will choose the language you want like:

```
Select a number for worker runtime:
1. dotnet
2. node
3. python
4. powershell
5. custom
Choose option:
```

In this tutorial we will use Python. Tip 3 and the project will be created.

### 3. Creating a function

In the step 2 we just started a functions but didn't create it yet.
To create the function we need to run:

```
func new
```

As this tutorial we gonna use the ServiceBus as a trigger, choose the option 11.

```
Select a number for template:
1. Azure Blob Storage trigger
2. Azure Cosmos DB trigger
3. Durable Functions activity
4. Durable Functions HTTP starter
5. Durable Functions orchestrator
6. Azure Event Grid trigger
7. Azure Event Hub trigger
8. HTTP trigger
9. Azure Queue Storage trigger
10. RabbitMQ trigger
11. Azure Service Bus Queue trigger
12. Azure Service Bus Topic trigger
13. Timer trigger
Choose option: 
```
After that, whe must choose the project name:

```
Azure Service Bus Queue trigger
Function name: [ServiceBusQueueTrigger] 
```

Well done, your function is already created!

### 4. Test it locally

For test it in your computer, run the command

```
func start
```

This will start your function and you can test using the python script on ```event-sender``` folder.
You just need to follow the step 6 from Setup.

### 5. Deploying it with Keda.

For deploy it in your AKS your just need to follow the step 2 to 5 from the Setup.
