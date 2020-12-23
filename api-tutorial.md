# API Tutorial

### What is an API?
API is an acronym for `Application Programming Interface`.
-    An API is an interface which can allow for software intermediaries to communicate with one another.
        - APIs are most commonly associated with web-development, where an API can serve as an intermediary between frontend and backend code.
        - Most modern APIs adhere to HTTP and REST standards.
-   Many software as a service (SaaS) services provide APIs that allow clients to connect their programs to the service's.
       - (ex Twitter, Yahoo Finance, Skyscanner, Alpaca, etc.)

### What is HTTP?
HTTP is an acronym for `HyperText Transfer Protocol`.
-   HTTP is a protocol used to transfer files over the web.
	- HTTP utilizes TCP (Transmission Control Protocol) to do this.
- There is no need to have a deep understanding of HTTP for the purposes of this course.
      
### What is REST?
REST is an acronym for `REpresentational State Transfer`.
-   REST is a architectual style that uses existing technology and protocols of the Web.
-   REST systems are based off of requests and responses.
-   REST almost always *utilizes* HTTP because it's the standard for web-based protocols.
	   - **Warning :** You have most likely heard of "RESTful" APIs. The distinction between REST and RESTful can be murky, but RESTful is often used as an adjective to describe something that conforms to the REST architecture. In most scenarios, the two can be used interchangeably.
- REST's most important features are... : 
	- The requesting systems (the program you wrote) are able to make requests to access or manipulate web resources.
	- When making a request, you can send a header which is additional information about the request
		-  (ex you may need to send authentication tokens to get a response in the first place.)
    - There exists at least one endpoint (URL in most cases).
    - All operations are *stateless*. This means that the current state of the requester does not matter.
	- Data is returned (a response) in a lightweight data format such as `JSON`.
	- Utilizes `CRUD` operations for requests.

### What is CRUD?
CRUD is an acronym for `Create, Read, Update, Delete`.
-   CRUD operations are linked to their respective basic *HTTP Verbs*.
  	- POST : Create new data
    - GET : Read data
    - PUT : Update data 
    - DELETE : Delete data
-   These operations are important because they serve as the building blocks for communication between the requester and web resource.
-   When making a request, you will use one of these verbs.


### Combining Python and RESTful APIs
Important Python libraries and modules for RESTful APIs :
-   **requests**
     - a library that allows you to request files from a server using HTTP (HyperText Transfer Protocol)


### Example Python code using Requests
```python3
# import the necessary libraries
import requests

# request a file from an endpoint with the GET verb
raw_file = requests.get(url='https://example.com/test.json')

# request a file from an endpoint with the GET verb with headers
raw_file = requests.get(url='https://example.com/test.json', headers={'KEY-ID': something, 'SECRET-KEY' : something})

```

### Final Remarks
APIs are extremely important in our everyday lives.
-   Without APIs, many of the services we depend on will not work.
      - (ex phone weather services, many sms platforms, etc.)
-   APIs allow us to easily transfer data between different systems through the Web.
