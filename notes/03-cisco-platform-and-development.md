## Domain 3: [Cisco Platform and Development]

**Key concepts:**

**Cisco SDK**
- Created virtual environment in Terminal to use Meraki SDK
```bash
kenny@Kennys-MacBook-Air Documents % python3 -m venv meraki
kenny@Kennys-MacBook-Air Documents % source meraki/bin/activate
(meraki) kenny@Kennys-MacBook-Air Documents % pip install meraki

[notice] A new release of pip is available: 26.0.1 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
(meraki) kenny@Kennys-MacBook-Air Documents % pip install --upgrade pip
```

- Meraki DevNet sandbox was unavailable to run tests live
- Search SDK documentation for steps and requirements
```python
API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"  # demo read-only API key
import meraki
dashboard = meraki.DashboardAPI(API_KEY)

response = dashboard.organizations.getOrganizations()
print(response)
```

**UCS Manager**
- Unified Computing System; geared toward data centers; IaC
- UCS series servers and fabric interconnects
- UCS Manager is embedded in UCS Fabric Interconnects; HTML GUI
- UCS Management API (integrates with VM Ware, Microsoft, etc)
- Accepts XML (through Python or PowerShell)
- Cisco Intersight (updated to UCS Director)
- SingleConnect Technology: one physical link for all logical traffic (management, SAN, LAN, etc)

**UCS Director**
- Network orchestration; IaaS
- Deployment of servers, templates, monitoring, automation workflows, bare metal provisioning
    - Task: smalles unit of work within UCS Director (starting SSH session, provisioning VM, etc)
    - Workflow: a collecion of tasks; allows for complex operations through templates
    - Service Request statuses: Scheduled, Running, Blocked, Completed, Failed
    - Library: Largest unit of work; collections of workflows and tasks

**Intersight**
- Cisco Intersight Cloud Portal; requires an account
- "Targets" = Devices
- Receive API Key and RSA Key in the Intersight Portal

**Cisco Collaboration Platforms**
- Webex API: Receive Bearer Token in Webex documentation (valid for 12 hours)
- Documentation shows GET, POST, etc for all functions (Rooms, Reporting, Roles, etc)
- Webex Devices (ex: Room Kit) can be accessed through xAPI and SSH
- Unified Communication Manager (UCM): VoIP, messaging, video collaboration
 - Uses AXL (Administrative XML); pip install ciscoaxl
- Finesse: UC control center (GET {URL:port}/finesse/api/)

**Cisco Security Platforms**
- Firepower (Firepower Management Center): firewall, IPS, etc
 - Before interacting programmatically, generate token with POST and Basic Auth
    - Add x-auth token to header
 - Status, Device Clusters, System Inforomation, and many more
- Umbrella (Secure Internet Gateway); requires account to access Umbrella GUI
    - Tokens can be generated for Devices, Reporting, etc
    - Tokens need to be encoded in base64; add Organization ID to header and GET auth bearer token
- AMP (Advanced Malware Protection); formerly known as Secure Endpoint
- ISE (Identity Service Engine); IAM, network administration, access control for wired and wireless endpoints
- ThreatGrid (rebranded as Secure Malware Analytics); email appliance, web appliance, firewalls, etc
    - Static malware analysis: comparing files (does not run code) to known malware signatures
    - Runs the code (in a sandbox) to discover hidden contents
    - Up-to-the-minute threat intelligence feed
    - Edge-to-endpoint integration (AMP, IPS, Firewall, Meraki)
    - "Glovebox" is ThreatGrid's sandbox to run malicious code safely

**NX-OS**
- Use NXAPI (show feature | inc nxapi > enabled or disabled; conf t to enable)
- Uses JSON or XML; sends familiar CLI commands

**DevNet Resources**
- DevNet Sandbox: available for free online to test automation workflows. Always-on and reservation-only
- Code Exchange: Official DevNet code repositories
- Support and Forums: Knowledge base (free), Community Forum (free), Chat with DevNet (free), Developer support tickets (paid; *retiring*)
- Learning Labs: Similar to sandboxes, walkthrough instructions
- API Documentation: developer.cisco.com/docs; official repository for all Cisco API info across all platforms

**YANG Data Modeling**
- Commonly used with NETCONF; no need to use specific Cisco, Juniper, etc commands --> "Data Modeling"
- Developed by IETF (RFCs 6020 and 6021)
- Namespac > Node > Leaf

**NETCONF**
- Intent-Based Networking
- Instead of Client-Server, NETCONF is Manager-Agent; uses YANG encdoded in XML, transported by NETCONF
- NETCONF's default port is 830

**RESTCONF**
- Similar to Client-Server using HTTPS (Port 443)
- Also uses YANG wih XML *or* JSON

```text
CRUD Function   |   HTTP Verb   |   NETCONF Operation
Create          |   POST        |   <edit_config> (operation="create)
Read            |   GET         |   <get>, <get_config>
Update          |   PUT/PATCH   |   <edit_config> (operation="create/replace" or "merge")
Delete          |   DELETE      |   <edit_config> (operation="delete")
```

**Questions/gaps:**
- This section covered many, many different Cisco products. I'm not sure how well I need to know these, but I imagine the questions will be similar to "which service would be most appropriate to do ___?"