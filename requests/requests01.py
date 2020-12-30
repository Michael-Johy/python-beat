import requests as reqs

response = reqs.get("http://www.baidu.com?")

print(response.status_code)
