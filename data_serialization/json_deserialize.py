import json


# with open("data_serialization/friends.json", mode="rt", encoding="utf-8") as fr:
#     obj = json.load(fr)
#     print(type(obj))
#     print(obj)


json_string = """{"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 2323232]}"""

obj = json.loads(json_string)
print(type(obj))
print(obj)
