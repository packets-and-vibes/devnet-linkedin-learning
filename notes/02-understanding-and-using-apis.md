## Domain 2: [Understanding and Using APIs]

**Key concepts:**

#### Fundamentals of REST API
- REST = Representational State Transfer
- Authentication:
    - Basic Authentication (no encryption; use SSL or TLS)
    - API Key Authentication (PSK; key is susceptible to interception)
    - OAUTH (Uses generated token from authentication server; token determine scope and lifespan)
- API Structure:
    - 1) URL (Uniform Resource Locator)
    - 2) Method (POST, GET, PUT, UPDATE, PATCH, DELETE)
    - 3) Request Header (HTTP header; formatted in key:value pairs)
    - 4) Body (data of the message)

#### Webhooks
- "Reverse APIs"
- HTTP POST messages triggered by an event; provides event notifications
- Example: e-commerce to retail store. APIs would create constant polling; webhook will notify only when triggered
- Requires URL; application with webhook must be running constantly

#### REST Constraints
- 1) Uniform interface
    - Identification of resources
    - Manipulation of resources
    - Self-descriptive messages
    - Hypermedia as the Engine of Application State (everything needed to use a website is included in its code)
- 2) Stateless (server does not store information about previous actions; every request is new)
- 3) Cacheable or non-cacheable label
- 4) Independent clients and servers
- 5) Layered system (proxy servers, load balancers; should be transparent to the client)
- 6) Code-on-demand (client downloads from server for execution)

#### HTTP Responses
- 1XX codes - Informational
- 2XX codes - Success
- 3XX codes - Redirection
- 4XX codes - Client side error
- 5XX codes - Server side error
    - 101 Continue (interim response)
    - 200 OK (Request successful)
    - 301 Moved permanently (new URI)
    - 302 Found
    - 304 Not modified
    - 400 Bad request (server was not able to interpret; likely syntax error)
    - 401 Unauthorized (not authenticated)
    - 403 Forbidden (server understood request, authenticated; not authorized)
    - 404 Fot found
    - 408 Request timed out
    - 500 Internal server error
    - 502 Bad gateway (bad response form upstream server)
    - 503 Service unavailable (could be DoS or server offline)

#### Posman Practice
```text
In Postman: GET https://postman-echo.com/get?test=123

### Output shown is data requested by the client

Status: 200 OK
{
    "args": {
        "test": "123"
    },
    "headers": {
        "host": "postman-echo.com",
        "user-agent": "PostmanRuntime/7.54.0",
        "accept": "*/*",
        "accept-encoding": "gzip, br",
        "postman-token": "85a10b2c-ad7a-4518-8d54-effc794df961",
        "cache-control": "no-cache",
        "x-forwarded-proto": "https"
    },
    "url": "https://postman-echo.com/get?test=123"
}
```

#### API Authentication

**Basic authentication**
```text
GET https://postman-echo.com/basic-auth > Returns 401 Unauthorized when no authentication is used

 # added username and password provided by Postman > Returns 200 OK
Body:
{
   "authenticated": true
}
```

**Token Authentication**
- Known as "Bearer Token"
- Consult API documentation for details (example of creating new (POST) GitHub repo in Postman)

**API Key Authentication**
- Less secure; typically used for project. Example: OpenWeather
```text
GET https://api.openweathermap.org/data/2.5/weather?lat=47.5053&lon=111.3008&appid=d3d972761dd7145f559367a31e76XXX

appid:api-key can be added in Authorization tab in Postman instead of URL
```

**Common API Styles**
- Remote Procedure Calls (RPC)
    - REST performs CRUD HTTP methods ("Resource-oriented)
    - RPC only uses GET and POST ("Action-oriented)
    - Legacy method used before REST
    - Request-response model (similar to Python functions)

**Synchronous vs. Asynchronous**
- Synchronous: real-time (example: voice calls)
    - Client must wait for a response before continuing
- Asynchronous: Communication not in real-time (example: emails)
    - Client can function normally while request is processed
- REST APIs are not exclusively synchronous or asynchronous; can be either based on use case

**Questions/gaps:**
- I have seen json.dump, json.dumps, etc. This course did not cover these functions at all. I think these are required for the exam so I will continue looking and supplement as needed.