
# Networking

## Protocols

The [Internet Protocol Suite](https://en.wikipedia.org/wiki/Internet_protocol_suite) is the set of communications protocols that drive the web. A communications protocol is just a set of rules for sending and receiving data. The protocols are arranged into layers, with each layer representing an abstraction on top of the last. An alternative to the 5-layer TCP/IP model is the [7-layer OSI model](http://www.electronicdesign.com/what-s-difference-between/what-s-difference-between-osi-seven-layer-network-model-and-tcpip). [img](https://en.wikipedia.org/wiki/Internet_protocol_suite#/media/File:IP_stack_connections.svg)

| Protocol | Layer | Description |
| ---      | ---   | --- |
| HTTP, FTP, SMTP, SSH, DNS | Application | applications that retrieve web pages, send mail, etc |
| TCP, UDP | Transport | make client-server connections, control transmission speed, check for errors |
| IP (v4 & v6) | Internet/Network | route packets between networks |
| Ethernet | Data Link/Link | route packets between nodes |
| IEEE 802.3u	| Physical| electrical pulses on a wire |


The two main protocols of the Transport layer are TCP [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) and UDP [User Datagram Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol). UDP is unreliable, but involves less overhead and is quicker, TCP is more reliable, but slower. TCP is built upon UDP, but UDP is still useful by itself for circumstances where some loss of data is acceptable, for example: audio and video chatting. If a microsecond of audio cuts out or distorted, it won't make much difference, whereas missing section of an executable can be catastrophic.

```
UDP
    -> request
    <- response
TCP
    -> open connection
    <- handshake
    -> request
    <- response
```

## Ports

Port: A port is a place in a computer where a process can connect to the network. There are 2^16=65536 ports on a computer. Below are the common ports of some protocols.

- 20/21 FTP
- 22 SSH (Secure Shell)
- 25 SMTP (Simple Mail Transfer Protocol)
- 53 DNS
- 80 HTTP
- 443 HTTPS

## Terms

Socket: an endpoint of a network, connects to a process on a port, allowing that process to send and receive data. Sockets operate in the application layer.

TCP/IP: the fundamental communications protocol (a standardized way of sending and receiving data) for the web.

Packet: A small segment of data which contains headers indicating the sender and receiver.

HTTP: Hypertext Transfer Protocol, rests on top of TCP/IP.

FTP: File Transfer Protocol, also rests on top of TCP/IP.

Client-Server Model: the standard architecture of the web, allows centralization of information in servers which many clients can access simultaneously, as opposed to the peer-to-peer model.

URL: Uniform Resource Locator, aka a web address. For example, `http://www.example.com/index.html`, `http` is the protocol, `www.example.com` is the hostname, and `index.html` is the file. [more info](https://en.wikipedia.org/wiki/URL#Syntax), [example image](https://doepud.co.uk/images/blogs/complex_url.png).

IP Address: a numerical address assigned to each device that's connected to a network. A dynamic IP can change over time, and may be different every time the device is connected to the network. Most users have dynamic IPs. A static IP is constant, and is used by servers hosting websites. An IP address may also have a port specified. An IPv4 address consists of 4 numbers, each in the range from 0 to 255 (the max value of 1 byte). [IPv6](https://en.wikipedia.org/wiki/IPv6) greatly expanded the number of available IP addresses.

DNS: Domain Name System, a collection of servers that maintain a mapping between IP addresses and hostnames. When you type an address 'www.google.com' into your address bar and hit enter, your browser looks up the IP address for that hostname by querying the DNS. Then your browser executes a GET on the IP to get the web page. [graphic](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Example_of_an_iterative_DNS_resolver.svg/500px-Example_of_an_iterative_DNS_resolver.svg.png) [more info](https://en.wikipedia.org/wiki/Domain_Name_System)


HTML: Hypertext Markup Language, a way of formatting elements on a web page.

CSS: Cascading Style Sheets, a way to add color, style, and animation to HTML.

JavaScript: a scripting language with superficially similar syntax to Java, may be used for both the front-end and back-end.

API: Application Programming Interface, an interface to an application, most often used in the context of Web APIs, which receive and respond to http requests.

AJAX: Asynchronous JavaScript And Xml, the ability to perform an HTTP request from

JSON: JavaScript Object Notation a way of encoding data that's similar to JavaScript objects, except you use strings instead of properties, and values can only be numbers, strings, arrays, or other objects.

Database: a collection of data, stored and retrieved through queries.

Front-End: code that runs on the client (in your browser), which usually consists of JavaScript, HTML, and CSS.

Back-End: code that runs on the server, deals with data processing, files, and databases and can involve a variety of different languages.



## Request-Response Cycle

The three parts of an HTTP message: the status line, headers, and body. The status line contains the request method or response code. The headers contain metadata, such as the [mime type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the data in the body, username and password, API keys, etc. The body contains the main bulk of data. You can read more about HTTP messages on the [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages).

![parts of a url](https://doepud.co.uk/images/blogs/complex_url.png)

You send an HTTP GET request whenever you type a URL into your address bar and hit 'enter'. You can see the body of the response by right clicking -> view page source. You can see the headers of the request and response on the "network" tab of the developer panel.

### Request Methods

HTTP requests include a **method**, which indicates the intention of the request. These methods are conventional. You could use `GET` to delete an entry in the database, but you shouldn't. You can find more info [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), [here](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods). The most common HTTP methods parallel the CRUD operations we discussed in Python.

| CRUD     | HTTP Method | SQL    |
| ---      | ---         |---     |
| Create   | POST        | INSERT |
| Retrieve | GET         | SELECT |
| Update   | PUT         | UPDATE |
| Delete   | DELETE      | DELETE |


### Response Codes

The response to an HTTP request will have a **status code** which indicates whether the request was successful or not, and what the error was. You can find a more thorough list of status codes [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

| Code | Description  | Examples
| ---  | ---          |---
| 1XX  | information  | |
| 2XX  | success      | 200 OK |
| 3XX  | redirection  | 301 Moved Permanently |
| 4XX  | client error | 403 Forbidden, 404 Not Found |
| 5XX  | server error | 500 Internal Server Error |



## Web Application Frameworks


| Framework | Language |
|--- |--- |
| Django, Flask | Python |
| Ruby on Rails | Ruby |
| ASP.NET | C# |
| Node.js | JavaScript |
| Apache Struts | Java |


