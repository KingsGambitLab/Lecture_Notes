## Topics to be covered
- **Why do we need Kubernetes in modern production systems ?**
- **What is Kubernetes, and how does it work ?**
- **Understanding key Kubernetes terms and concepts.**
- **Learning how to orchestrate applications effectively using Kubernetes.**

---

## Why Kubernetes?

### Understanding the Need for Kubernetes in Production Systems

1. **Software System Architecture:**
    - Modern software systems are rarely built as single, large applications (commonly known as **Monolithic Architecture**). Instead, they are often broken down into smaller, independent units called **Microservices**.
    - Each microservice typically runs multiple instances to handle varying loads and ensure reliability. These instances need to be deployed across many servers.

2. **Deployment Approaches:**
    - **One Server per Instance**:
        - In this approach, we allocate a single server for each microservice instance.
        - **Advantages**: This method is simple to manage since every server runs a single instance, making it easier to monitor and maintain.
        - **Disadvantages**: This setup can lead to **resource under-utilization**. If a service doesn't need all the available resources on a server, the remaining capacity goes unused, leading to inefficient use of hardware and higher infrastructure costs.
  
    - **Multiple Instances on a Single Server**:
        - This approach allows multiple microservice instances to run on the same server, improving resource utilization.
        - **Challenges**: It introduces complexity. A lot of planning is required to determine which applications or instances can coexist on the same server without causing conflicts or resource bottlenecks.
  
3. **Scaling Challenges at Large Enterprises**:
    - Consider large companies like Google, which might run **1000+ services** and **50,000+ instances** distributed globally across data centers. 
    - **Human intervention is impossible at such scale**. Managing and monitoring the distribution of services across thousands of servers would be overwhelming.
    - This is where **automation** becomes crucial, and manual methods fail to cope with the dynamic nature of resource allocation.

4. **Need for Orchestration**:
    - Think of an **orchestra**: a group of musicians playing different instruments. A **conductor** ensures that every musician plays in harmony. 
    - In the context of software, there are thousands of microservice instances (instruments) running on numerous servers (musicians). These need to work together seamlessly.
    - The tool that serves as this "conductor" in modern, cloud-native architectures is **Kubernetes**, which **orchestrates** the deployment, scaling, and management of applications across distributed systems.

---

## What is Kubernetes?

### Overview of Kubernetes

- **Kubernetes** (often abbreviated as **K8S**) is an open-source system for automating the deployment, scaling, and management of containerized applications. It was launched by Google in **2015**, following years of experience managing its own internal systems through a similar technology called **Borg**.
    - **Borg** has been in use at Google since 2004 and continues to manage Google's internal microservices across data centers.
    - Kubernetes was developed to solve similar orchestration challenges but was designed as a general-purpose tool that could be used by any organization to manage containerized applications.

- **Key Functionality of Kubernetes**:
    - **Inputs**: 
        - Configuration of the services that need to be deployed (e.g., the number of instances of each service).
        - Information about the available servers (the physical or virtual machines where services can run).
    - **Outputs**:
        - Kubernetes dynamically assigns services to servers based on load and resource availability, ensuring the most efficient use of resources across the infrastructure.
  
- **Fundamental Role of Kubernetes**:
    - **Efficient Resource Utilization**: Kubernetes ensures that resources (CPU, memory, etc.) are utilized optimally across all servers.
        - For example, if one server is under heavy load while another is idle, Kubernetes can move services to balance the load.
    - **Health Checks and Recovery**: Kubernetes continuously monitors the health of running services. If a service becomes unresponsive, Kubernetes can automatically restart it or move it to a healthier server.
  
### Additional Features of Kubernetes

- **Cloud Integration**:
    - Kubernetes has built-in capabilities to integrate with popular cloud providers such as **AWS**, **Google Cloud**, and **Azure**. 
    - When additional resources are needed (e.g., more servers or instances), Kubernetes can automatically communicate with the cloud provider’s API to provision or decommission servers as necessary.

- **Auto-scaling**:
    - Kubernetes supports **horizontal auto-scaling**, similar to the functionality provided by cloud services like **AWS Elastic Beanstalk**. 
    - Based on specified parameters (e.g., CPU utilization), Kubernetes can automatically adjust the number of instances running for a particular service.
    - This ensures that services can handle increased traffic without manual intervention.

---

## How Kubernetes Works

### The Architecture of Kubernetes

- To manage an application across many servers, you need an overarching system that can coordinate where each instance of your application runs. This is what Kubernetes achieves through its **cluster** architecture.
  
- **Kubernetes Cluster**: A collection of servers (also called **nodes**) managed by Kubernetes.
    - **Worker Nodes**: These are the servers that run the actual application services (e.g., product service, payment service).
    - **Control Plane (Master Node)**: This node is responsible for managing the overall cluster, making decisions about where services should be deployed, scaling applications, and monitoring the health of the system.

### Key Components of the Control Plane

1. **Scheduler**:
    - The scheduler is responsible for assigning services to worker nodes. It checks which nodes have the capacity to handle new service instances and schedules them accordingly.
    - It also continuously monitors the health of nodes. If a node goes down, the scheduler reassigns the services running on that node to healthy ones.

2. **Cloud Manager**:
    - This component interacts with cloud providers to provision or destroy servers based on the needs of the cluster.
    - For example, if more server capacity is needed, the cloud manager can request additional servers from **AWS** or **Google Cloud**.

3. **ETCD Database**:
    - **ETCD** is a distributed key-value store used by Kubernetes to store all the configuration data for the cluster.
    - It holds important information such as:
        - Service names
        - Deployment rules
        - Resource constraints
        - Server and instance details

**Diagram Reference**: The diagram below illustrates the high-level architecture of Kubernetes, including the relationship between the control plane and worker nodes.
![K8S Architecture](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/692/original/1.png?1725546608)

- **Worker Nodes**:
    - Each worker node runs services inside **Pods** (the smallest deployable units in Kubernetes, containing one or more containers).
    - A service called **Kubelet** runs on each worker node, allowing it to communicate with the control plane.
    - Multiple pods can run on a single node, and each pod may contain one or more containers running the actual application.

---

## Key Kubernetes Terms

### Important Kubernetes Concepts and Terminology

1. **Node**:
    - A **Node** is a machine (physical or virtual) in a Kubernetes cluster. 
    - There are two types of nodes:
        - **Control Plane Node (Master Node)**: Responsible for managing the cluster and making decisions about where services should run.
        - **Worker Node**: Runs the application services.

2. **Pod**:
    - A **Pod** is the smallest deployable unit in Kubernetes. It typically contains one or more containers, which are instances of your application.
    - **Pods** provide isolation between applications, ensuring that each service has its own set of resources and dependencies.
    - Kubernetes doesn’t directly manage containers (like Docker does); instead, it manages containers through pods, allowing it to work with any container runtime, not just Docker.

3. **Deployment**:
    - A **Deployment** is a configuration file (typically written in YAML) that describes how Kubernetes should run an application.
    - It specifies things like:
        - Which application to run (the container image).
        - How many instances of the application should be running.
        - The resource requirements for each instance.

4. **Service**:
    - A **Service** is a network configuration in Kubernetes that defines how external clients interact with the application.
    - A service routes requests to the appropriate **pods** (often through a load balancer) and ensures that traffic is evenly distributed across the available pods.

    **Example**: If your application runs on port **8080** internally, a service can map external requests on port **80** (HTTP) to port **8080** of the pod.

    ![Service Example](https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/088/693/original/2.png?1725546653)

- Kubernetes can automatically scale the number of pods running based on the load, and it can distribute traffic evenly among the available pods.

---

## Practical Demonstration

### Steps for Setting Up a Kubernetes Cluster Locally

1. **Installing Minikube**:
    - Ask students to install **Minikube** (a tool that allows you to run a Kubernetes cluster locally). It will simulate a full Kubernetes environment on their local machines. 
    - Installation guide: [Minikube Installation](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download)

2 **Checking Kubernetes**:
  * Once Minikube is installed, ensure Kubernetes is running by executing:
    ```bash
    kubectl get pods
    ```
    * This command will list the running pods on the Kubernetes cluster.

3. **Deploying a Service**:
    - Create two **YAML** configuration files: one for **Deployment** and another for **Service**.
    
    - **Deployment Configuration**:
        - Name: `productservice`.
        - Set **replicas** to **5** (indicating 5 instances of the service should run).
        - Specify the container image (e.g., a **Spring Boot** application).
    
    - **Service Configuration**:
        - Name: `ProductService_Service`.
        - Expose the service on **port 3000** and forward traffic to the application running inside the container on **port 8080**.
        - Set the service type as **LoadBalancer**.

4. **Running the Configuration**:
    - Deploy the application by running the following commands:
    ```bash
    kubectl apply -f ProductServiceDeployment.yaml
    kubectl apply -f ProductService_Service.yaml
    kubectl get pods
    ```

5. **Demonstrating Auto-recovery**:
    - Try deleting one of the pods to simulate a failure:
    ```bash
    kubectl delete pod <pod_name>
    ```
    - Kubernetes will automatically create a new instance of the deleted pod, maintaining the desired number of replicas.

6. **Accessing the Application**:
    - Retrieve the IP address of the load balancer by running:
    ```bash
    minikube service productservice --url
    ```
    - Open this URL in a browser to see the running **Spring Boot** application, which is automatically load-balanced across multiple instances.

7. **Viewing the Kubernetes Dashboard**:
    - Open the Kubernetes dashboard to get a visual overview of the cluster's status:
    ```bash
    minikube dashboard
    ```

8. **Viewing Logs**:
    - You can also inspect the logs of any running pod to debug or monitor the application's performance.

### Further Reading

- official documentation for a deeper understanding of:
    - **[Pods](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)**.
    - **[Deployments and Services](https://kubernetes.io/docs/concepts/services-networking/service/)**.

