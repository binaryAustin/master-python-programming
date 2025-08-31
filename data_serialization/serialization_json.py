import json

friends = {"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 2323232]}


# with open("data_serialization/friends.json", mode="w", encoding="utf-8") as fw:
#     json.dump(friends, fw)


json_string = json.dumps(friends)
print(json_string)
