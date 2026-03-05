import json

new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99
}

with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total books:", len(inventory))

inventory.append(new_book)

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

for book in inventory:
    print(book)