## Domain 4: [Application Deployment and Security]

**Key concepts:**

**Application Deployment Models**
- Cloud Service Models
    - IaaS: virtual provisioning of resources available over the internet (compute, network, storage)
    - Paas: Used for app creation; supports complete web application lifecycle & development tools
    - SaaS: Quick access to cloud-based web applications

- Cloud Deployment Models
    - On-Demend Self-Service: Requested resources are automatically processed (AWS EC2); fast deployment
    - Broad Network Access: PCs, Mac, tablets
    - Resource Pooling: storage, compute, network, etc are pooled; offers savings
    - Rapid Elasticity: Provision and tear down as needed
    - Measured Service: CSP is monitored; usage-based plans
- Private Cloud: only used by one user; security and privacy; more expensive
- Public Cloud: Provisioned for open use; cost effective, less secure
- Community Cloud: Private cloud variation (GovCloud); no concrete standard
- Hybrid Cloud: Combine two or more models; example: on-prem/public deployment

- NIST Cloud Reference Architecture
    - NIST SP 500-292
    - Cloud Provider: responsible for providing cloud services
        - Resource Abstraction and Control Layer: CSP is providing reliable access and experience
        - Physical Resources: Cooling, firewalls, etc
        - Cloud Service Management: Business Support, Provisioning & Config (SLAs), Portability and Interoperability
        - Security & Privacy
    - Cloud Consumer
    - Cloud Broker: Service Intermediation, Service Aggregation, Service Arbitrage
    - Cloud Carrier: Telco between CSP and end users
    - Cloud Auditors: Security Audit, Privacy Audit, Performance Audit

- Edge Computing
    - Geographical edge of the network; near to the devices accessing or using data
    - Coast savings due to shorter transport and centralized power
    - Security and privacy
    - Extend resources outside of the traditional data center

- Application Deployment Types:
    - Hypervisors: Provisions VMs; Type I: bare metal, Type II: runs on top of operating system
    - VMs: Guest OS, support files, and applications. Not only PCs and servers; network appliances can be virtualized
    - VMs create additional overhead; containers are packages of applications, software and libraries
        - Run on a single OS, share host resources
        - Less resource intensive and less storage required than VMs
        - Risks: Resource Isolation (restrict communication between containers); larger attack surface; vulnerable source code; obscured visibility
    - Serverless Computing: No server provisioning required (servers are not exposed to the end customer)
        - FaaS (Function as a Service): PaaS uses resources that are constantly running; FaaS executes code on-demend
        - AWS Lamda: general purpose serverless compute engine
        - AWS Fargate: runs Docker containers; latency-sensitive

**Application Deployment Considerations**

- DevSecOps Principles: movement from Waterfall to Agile; CI/CD pipelines; integrates security early in development
- Python Unit Test: import unittest; create tests for Python code; allows you to alter test script instead of source code

**Docker Images and Containers**
- "containerd" runs Docker in Linux
- Dockerfile (Needs to be capitalized): text document that contains all commands to run Docker images
    - FROM ubuntu
    - MAINTAINER support@mail.com
    - RUN apt-get update
    - RUN apt-get install nginx -y
    - EXPOSE 80
    - VOLUME /usr/share/nginx/html
    - CMD ["nginx", "-g", "daemon off;"]

**Vulnerability Stack & Web App Threats**
- Vulnerability Stack:
    - Security (Firewall/IPS)
    - Network (Routers/Switches)
    - Operating System (Winows/Linux/Mac)
    - Databases (Oracle/MySQL/MS SQL)
    - Web Servers (Apache/IIS)
    - Third-Party Components (Webb apps)
    - Custom Apps (Business-specific)

Web Application Threats:
- SOAP (Simple Object Access Protocol); relies on XML; stored in plain text
- REST (RESTful) Services; modern alternative to XML; HTTP verbs (CRUD)
- OWASP Top Ten (list of common web vulernabilities)
    10. Server Side Request Foergery (SSRF)
    9. Security Logging and Monitoring
    8. Software and Data Integrity Failures
    7. Identification and Authentication Failures
    6. Vulnerable and Outdated Components
    5. Security Misconfigurations
    4. Insecure Design
    3. Injection
    2. Cryptographic Failures
    1. Broken Access Control

**Bash Commands**
- pwd (print working directory)
- cd (change directory; cd with no parameter goes to home;)
- ls (list files; -a shows hidden files)
- mkdir (make directory)
- rm (remove a file, NOT directory; rm -rf removes everything)
- touch (create a file)
- cat (concatenate; displays contents of a file)
- vim (open file to edit; :wq to write and quit)
- mv (move or rename)
- cp (copy)
- .sh is a best practice when creating a script in Linux
    - Start with #!/bin/bash
    - # This is a simple bash script
    - echo "Hello, World"
- chmod (change/modify permissions)
    - chmod 111 hello.sh (everyone only has execute only)
    - chmod 222 hello.sh (everyone can write only)
    - chmod 774 hello.sh (admin/group can rwx; anyone else can only read)

**Questions/gaps:**
- The cloud section was very easy and largely review. I'm curious o see how deeply I'll need to understand the vulnerability stack. I understand the basic concepts well, but not in great detail. I imagine these will be covered in much greater detail in the CyberOps exam.