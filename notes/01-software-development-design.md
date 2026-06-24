## Domain 1: [Software Development and Design]

**Key concepts:**

#### XML
    - Extensible Markup Language
    - HTML uses pre-defined tags; XML has no pre-defined tags
    - Allows commenting
    - XML data example:
```xml
<network>
    <name>Chicago - Wireless Network</name>
    <total_usage_kbytes>98446004</total_usage_kbytes>
    <total_user_count>286</total_user_count>
    <node>
        <mac>77:40:b8:0E:71:5E</mac>
        <name>Catalyst-9136</name>
        <lat>41.8781</lat>
        <lng>87.6298</lng>
        <channel>36</channel>
    </node>
</network>
```

    - Elements can be alphanumeric; have to start with a-z or _; case sensitive; no space allowed

#### JSON
    - JavaScript Object Notation
    - Gaining popularity in network automation
    - Cisco DNA Center (Catalyst Center) expects incoming JSON data
    - Data is formatted in Key:value pairs; does not allow commenting; whitespace does not matter
    - JSON data example:
```json
{
    "employees":[
        {"firstName":"John", "lastName":"Smith"},
        {"firstName":"Susan", "lastName":"Wright"},
        {"firstName":"Mark", "lastName":"Adams"}
    ]
}
```

#### YAML
    - YAML Ain't Markup Language
    - Hierarchical format
    - Key:value pairs for differentiating data
    - YAML is case sensitive; whitespace is critical; can be used with JSON data
    - YAML data example:
```yaml
        nodes:
          - id: n1
            label: SW1
            node_definition: iosv12
            condifugration: null
            interfaces:
              - id: i1
                slot: 1
                label: GigabitEthernet0/1
                type: physical
          - id: n2
            label: R1
            node_definition: iosv
            configuration: |-
              Building configuration...

              Current configuration : 1361 bytes
              !
              ! Last configuration change at 14:21:40
```

- Basic XML, JSON, and YAML Parsing
- Software Development Methods:
    - Test-Driven Development (TDD): testing happens first; tests small sections and functions of code
        - 1) Write a unit test
        - 2) Unit test fails
        - 3) Write code to pass the test
        - 4) Unit test passes
        - 5) Refactoring (remove hardcoded variables, etc)
    - Agile: Minimizes risk (dubget, bugs, etc); iterative, incremental releases based on feedback
        - Individual and interactions order processes and tools
        - Working software over comprehensive documentation
        - Customer collaboration over contract negotiation
        - Response to change over pre-determined plans
        - Product backlog > Sprint Planning > Sprint Cycles/Daily Scrum > Working Version > Customer Feedback ...
    - Lean Method: Basis for Agile; not a modern development framework
        - Elimination of waste (unneeded features, bugs)
        - Just-in-time
        - Continuous improvement (Kaizen)
        - 1) Identify Value
        - 2) Map the Value Stream
        - 3) Create Flow
        - 4) Establish Pull
        - 5) Seek Perfection
    - Waterfall Method: More rigid approach; each phase must be completed before the next
        - The end product is designated at the beginning (does not handle change well)
        - No value is created until the end of the process
        - Quality can be challenging due to lack of timely feedback
        - 1) Requirement Gathering
        - 2) System Design
        - 3) Coding
        - 4) Testing
        - 5) Deployment
        - 6) Maintenance

### Organizing Code
Python functions --> def func1(): / def func2(argument)
Python classes --> instantiate your class with ```__init__```

```python
class Date:
    def __init__(self, month, day, year)
    self.month = month
    self.day = day
    self.year = year

p1 = Date("February", 11, 2022)
print(p1.month)
print(p1.day)
print(p1.year)
```

Python modules
```python
import math
print(math.sqrt(25))

import calendar
print(calendar.month(2022, 2))

# Create own module / create modules.py
def hello(name):
    print("Hello, " + name + "!")

import modules

modules.hello("Kenny")
```

### Software Design Methods
- 1) Model-View-Controller: View (UI), Model (Data Mgmt), Controller ("brains"). Common in web design; code is modular
- 2) Observer: Subscription-based model; one-to-many (social media update); one subject and one or more observers
- 3) Version Control: Tracking changes to a file or files

**Questions/gaps:**
- Need to continu refining my knowledge around the uses and differences between classes, modules, etc.
    - Follow up with 100 Days of Code topics or other learning resources