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

## Create a Python Image

Follow steps outlined in article below:
https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/

Same Files (with environment.yaml) are also given in 
py\k8_starter

Using python locally (on port 5000): 
- create enviornment using  app\environment.yaml
- run main.py
<pre>python main.py </pre>
- check the output in
    http://localhost:5000/


Using Docker (on port 5001) : 
- create an image using following command
<pre>docker build -f Dockerfile -t hello-python:latest .</pre>
- run docker container using:
<pre>docker run -p 5001:5000 dynacard-flask</pre>
- check the output in
    http://localhost:5001/

## Python in minikube (Aborted Route)

https://minikube.sigs.k8s.io/docs/start/


Deploy an Application using NodePort (No Luck):
    Delete service if exists:
        kubectl delete service hello-python-service
        kubectl delete deploy hello-python-service

    kubectl create deployment hello-python-service --image=hello-python:latest
    kubectl expose deployment hello-python-service --type=NodePort --port=5000
    kubectl get services hello-python-service

    Deploy a service:
        minikube service hello-python-service
    Alternatively, port forward using:
    kubectl port-forward service/hello-python-service 6000:5000

    No luck due to:
    https://github.com/kubernetes/minikube/issues/9030

Deploy an Application using LoadBalancer (No Luck):

kubectl create deployment balanced --image=hello-python
kubectl expose deployment balanced --type=LoadBalancer --port=5000

minikube tunnel
kubectl get services balanced

## Python in Kubernetes 

https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/
Understanding Kubernetes by an example python application. 


Other useful commands
<pre>
    kubectl delete deploy hello-python-service
    kubectl delete service hello-python-service
    kubectl delete pods --all
</pre>

Run using Kubernetes (on port 6000) : 
- verify your kubectl is configured. At the command line, type the following:
    <pre>
        kubectl version
    </pre>
    - If you don’t see a reply with a Client and Server version, you’ll need to install and configure it.

- If running on Windows or Mac, make sure it is using the Docker for Desktop context by running the following:
    <pre>
        kubectl config use-context docker-desktop
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
    - The service is NOT working in my network as 6000 port is potentially reserved. See link below
        - 
    - 

- View the services available and description for the service
    <pre>
        kubectl get services
        kubectl describe service <hello-python-service>
    </pre>

- debugging application
https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/
<pre>
    kubectl get endpoints hello-python-service
</pre>

Get all the resources in default namespace
<pre>
    kubectl get all -n default
    kubectl describe pod -n default <pod name>
</pre>

Other references:
https://betterprogramming.pub/getting-started-with-kubernetes-for-python-254d4c1d2041
https://medium.com/avmconsulting-blog/running-a-python-application-on-kubernetes-aws-56609e7cd88c


## References

https://azure.microsoft.com/en-us/overview/kubernetes-getting-started/
https://www.youtube.com/watch?v=X48VuDVv0do
https://spot.io/blog/azure-kubernetes-the-basics-and-a-quick-tutorial/

https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/

https://www.mydistributed.systems/2021/12/holiday-reading-list-2021.html


