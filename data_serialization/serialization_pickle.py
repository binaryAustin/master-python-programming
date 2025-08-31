import pickle

friends = {"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 2323232]}


# with open("data_serialization/friends.dat", mode="wb") as fw:
#     pickle.dump(friends, fw)


with open("data_serialization/friends.dat", mode="rb") as fr:
    obj = pickle.load(fr)
    print(type(obj))
    print(obj)
