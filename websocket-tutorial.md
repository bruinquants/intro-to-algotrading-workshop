# WebSocket Tutorial

### What is a WebSocket?
A WebSocket is a persistent connection between a client and a server.
-    A WebSocket API has distinct differences from the RESTful APIs that we learned about earlier. 
        -  The main difference between the two is that WebSockets are stateful protocols. REST is stateless.
        -  A server may send data to the client when data is updated with WebSockets--this is different from REST where the client must request the information via HTTP.
-   Due to different protocols being used for WebSockets than for REST (HTTP), there is less overhead. Additionally, getting data from a server is no longer has to be a two-step process (Send a Request -> Wait for a Response)
        -   For this reason, WebSockets are almost always more efficient performance-wise.
-   **Question :** If WebSockets have better performance and simplifies pulling data, why would we ever use REST?
        -   The biggest reason is that HTTP requests are better supported throughout the web. More compatibility generally means easier integration.

### Why are WebSockets Important for Quant?
Because real-time quote data is *extremely* important for algos, WebSockets APIs can offer a faster and more efficient method of data transfer.
-   We could *technically* use a RESTful API to pull quote data in regular intervals, but this would be inefficent.
        -   **Remember :** WebSockets are a *two-way street*. The web resource (server) can send data to the client and vice versa.
-   Less overhead also means more scalability which could be important later down the road.

### Combining Python and WebSockets
Important Python libaries and modules for WebSockets :
-    **websocket**
        - a library that allows you to start a WebSocket connection.



### Final Remarks
WebSockets are not only useful, but almost ecessary when creating an algo.
-   WebSocket APIs solve some of the pitfalls of REST APIs.
-   In applications where streaming data is important, WebSockets are the way to go.