import requests

print(requests.__version__)

req = requests.get("https://raw.githubusercontent.com/the-rooster/Lab1Cmput404/master/script.py")

print(req.text)
