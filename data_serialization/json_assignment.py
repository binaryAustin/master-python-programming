import json
import requests


res = requests.get("http://jsonplaceholder.typicode.com/todos", timeout=10.0)

todos = json.loads(res.text)

for task in todos:
    if task["completed"] is True:
        print(task)
