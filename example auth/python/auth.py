from urllib import response
import requests

licensekey = "123"
id = "1"
url = f"http://127.0.0.1:5000/{licensekey}/{id}"

response = requests.get(url)

if response.json() == "false":
    print("access denied")
elif response.json() == "true":
    print("access granted")