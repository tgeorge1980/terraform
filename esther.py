import json

with open("george.json", "r") as file:
    data = json.load(file)

print("ID:", data["id"])
print("Name:", data["name"])
print("Age:", data["age"])
print("Email:", data["email"])