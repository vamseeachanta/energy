# Introduction

kubernetes or K8s is a way to run and orchestrate applications. 
kubernetes means pilot or 

# Summary

## How to practice Kubernetes:

In Developer Machine:
- Use Minikube (Needs Virtual Machine or Hyper-V)
- Alternatively use docker. See below link to enable kubernetes in Dockers. 
    - https://stackoverflow.com/questions/70127857/minikube-doesnt-start-on-windows-server-2019

In Cloud:
- Currently users 

## First Steps

## Tools Required

### kubectl

kubectl is Kubernetes command-line tool which facilities the following:
- run commands against Kubernetes clusters
- deploy applications
- inspect and manage cluster resources
- view logs

Install kubectl
https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/

Other references:
https://kubernetes.io/docs/reference/kubectl/cheatsheet/


### minikube

 minikube is a tool that lets you run Kubernetes locally. 
 minikube runs:
    - a single-node Kubernetes cluster on your personal computer (including Windows, macOS and Linux PCs) 
    - allows to try out Kubernetes, or for daily development work.
    - should NOT be used for production. users should be well aware of the limitations and pitfalls prior to use in production


Install minikube
https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/

Other references:
https://minikube.sigs.k8s.io/docs/start/

## Python in Kubernetes 

Follow steps outlined in article below:
https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/

Same Files (with environment.yaml) are also given in 
py\k8_starter

Understanding Kubernetes by an example python application. The different ways of running this application is summraized below:

Using python locally (on port 5000): 
- create enviornment using  app\environment.yaml
- run main.py
<pre>python main.py </pre>
- check the output in
    http://localhost:5000/

Using Docker (on port 5001) : 


http://localhost:5001/

Run using Kubernetes (on port 6000) : 
- verify your kubectl is configured. At the command line, type the following:
    <pre>
        kubectl version
    </pre>
    - If you don’t see a reply with a Client and Server version, you’ll need to install and configure it.

- If running on Windows or Mac, make sure it is using the Docker for Desktop context by running the following:
    <pre>
        kubectl config use-context docker-for-desktop
    </pre>
    - Got the error: 
        - error: no context exists with the name: "docker-for-desktop"
        - Checked the .Kube file in below folder:
            C:\Users\<username>\.kube\config
        - However, progressed to next step as no issues are encountered.
    
- View the node by typing to ensure Kubernetes is working:
    <pre>
        kubectl get nodes
    </pre>

- Use kubectl to send the YAML file to Kubernetes by running the following command:
    <pre>
        kubectl apply -f deployment.yaml
    </pre>
- Running pods can be viewed by executing following command:
    <pre>
        kubectl get pods
    </pre>
- View service at below:
    - http://localhost:6000
    - The service is NOT working


## References

https://azure.microsoft.com/en-us/overview/kubernetes-getting-started/

https://spot.io/blog/azure-kubernetes-the-basics-and-a-quick-tutorial/

https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/

https://www.mydistributed.systems/2021/12/holiday-reading-list-2021.html

