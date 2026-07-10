## Domain 5: [Infrastrucure and Automation]

**Key concepts:**

**Infrastructure Automation**
- Model-Driven Programmability: provides a unified standard (YANG) way of interacting instead of vendor-specific; client-server; this provides a common language

**Management**
- Controller-Level Management: Centralized platform for management instead of individual devices through CLI
    - Northbound: REST APIs
    - Southbound: Toward devices (SNMP, CLI)
    - Controllers can easily rollback changes
    - Some controllers have limitations and cannot perform all functions
- Device-Level Management: Traditional management; complete access to full device config
    - Time-consuming; more prone to mistakes
    - NETCONF and RESTCONF has helped management by using templates

**Network Simulation Test and Tools**
- CML: "VIRL" = CML; testing lab with many device and host instances accessible over Cisco VPN
- pyATS: Python testing library; available in CML
    - pyATS Library used to be called "Genie"
    - pip install pyats; Cisco GitHub has sample scripts

**Ifrastructure Automation Considerations**
- CI/CD Pipeline: Ongoing process of building, testing, staging, and releasing code
    - Uses version control throughout, like Git
    - CI: "Build server" is the brains (Teamcity or Jenkins)
    - Integrates with CSPs like AWS
    - CD: Automation of software release; build server provides support for CD
- IaC: Inspired by software development, but for infrastructure; Ansible, Chef, Puppet
    - Easily create identical environments or configurations; less errors due to replication
    - IaC Declarative Approach: Define the desired *end state* (AWS S3 template)
    - IaC Imperative Approach: Define a set of commands for execution (AWS S3 created through commands)
    - Terraform is a common IaC platform
- Automation Tools:
    - Chef: Open source (Ruby programming language)
        - Push Model: Management server pushes out configs to managed nodes
        - Pull Model: Nodes leverage an install agent to download configs from management server
        - *Chef uses pull*
        - "Recipe" = config information written in Ruby
        - "Cookbook" = Collection of recipes and other files used to facilitate automation
    - Puppet: Cisco's preferred orchestration tool; supports Catalyst and Nexus switches and UCS
        - Uses *pull model*
        - Server = "Puppet Master"; Client = "Puppet Agent"
        - Puppet Master contains all configs and Puppet codes; Linux
        - Puppet agents run on software on all OS; pulls configs through SSL connection
        - Resources = a description of the desired state
        - Manifests = Config used for program execution
        - Module = A collection of manifests used for an automation task
    - Ansible: Agentless; *uses push*
        - Uses YAML
        - Ansible Controller Machine = the only "smart devices"
        - Typically uses SSH, but can use Windows Remote Management (WRM)
        - Ansibile Inventory File = a list of nodes under management
        - Playbooks = Tasks written in YAML
        - Automation Engine = where users create Playbooks on Controller
        - Modules = Tasks invoked by Playbooks that are executed against nodes

- Bash Script Workflow
    - pthon3 -m venv meraki (virtual environment)
    - source meraki/bin/activate
    - export apikey=XXXXXXX (environment variable)
    - curl --location --request GET "https://api.meraki.com/api/v0/organizations" --header "X-Cisco-Meraki-API-Key: $apikey" (very long output) | jq (JSON output)
    - vim curl.sh
    - #!/bin/bash
    - #Grab Meraki devices
    - curl --location --request GET "https://api.meraki.com/api/v0/organizations" --header "X-Cisco-Meraki-API-Key: $apikey" | jq
    - chmod 774 curl.sh
    - ./curl.sh (runs script)

- Python Workflow
```bash
pip install requests
pip install urllib3
pip install prettytable
```
```python
ENVIRONMENT = "sandbox"
if ENVIRONMENT == "sandbox":
    dnac = {
            "host": "sandboxdnac2.cisco.com",
            "port": 443,
            "username": "devnetuser",
            "password": "Cisco123!"
            }
```
```python
from environment import dnac
import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable

dnac_devices = PrettyTable(['hostname', 'Platform Id', 'Software Type', 'Software Version'. 'Up Time'])
dnac_devices.padding_width = 1

headers =   {
                'content-type': "application/json",
                'x-auth-token: ""
            }

def dnac_login(host, username, password):
    url = "https://{}/apisystem/v1/auth/token".format(host) #will pass in the token later
    response = requests.request("POST", url, auth-HTTPBasicAuth(username, password))

    return response.json()["Token"]

```

- Ansible Playbook Workflow
    - Always check requirements.txt file (pip install -r requirements.txt)
    - View Yaml Playbooks; Playbook will explain the function
    - ansible-playbook -i inventory 01_aci_tenant_pb.yml

- Interpreting YANG Models
    - pip install pyang (view data in tree format)
    - pyang -f tree -o ietf-interfaces.txt ietf-interfaces.yang

**Code Review Process**

- Code Review
    - Gerrit: automated review tool (integrtes with Git)
    - SmartBear is used by Cisco for code review
    - Review less than 400 lines of code at a time; no less than 60 minutes per 400 lines
    - Code review cheklist: feature requirements? styles? Intuitive? Comments? Naming conventions? README?
    - Collaborative error correction is best

- Sequence Diagrams
    - Illustrate REST APIs in a visual manner
    - User > Login > Database (website login)
    - Solid lines = call / dashed lines = response