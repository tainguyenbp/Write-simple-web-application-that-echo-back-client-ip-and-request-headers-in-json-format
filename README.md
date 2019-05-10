Write simple web application that echo back client ip and request headers in json format.
The application should have properly logging setup for later audit, debug purpose.
o Eg:
$ curl http://abc.xyz/
{
 "Client IP": "192.168.1.10",
 "Host": "abc.xyz",
 "User-Agent": "curl/7.61.1",
 "Accept": "*/*"
}
