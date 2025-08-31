import requests


url = "https://www.python.org/"

res = requests.get(url, timeout=10.0)
