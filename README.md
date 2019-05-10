Write simple web application that echo back client ip and request headers in json format.
The application should have properly logging setup for later audit, debug purpose.
o Eg:

$ curl http://abc.xyz/

{

 "Client IP": "192.168.1.179",

 "Host": "abc.xyz",

 "User-Agent": "curl/7.61.1",

 "Accept": "*/*"

}

Cài đặt python3.6 trên centos7:

https://github.com/tainguyenbp/how-to-setup-python3.6-with-tools-ansible

Run web application with python:
python3.6 simple_web_application.py

Run bằng cách truy cập đến web:
http://192.168.1.196:5000/json

