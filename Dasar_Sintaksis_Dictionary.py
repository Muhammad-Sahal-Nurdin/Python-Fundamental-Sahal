import json
# Simbol dictionary ditandai dengan {}
# Harus dalam key
# Tidak boleh menggunakan angka
users = {
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz'
    # 'address': {
    # 'street': 'Kulas Light',
    # 'suite': 'Apt. 556',
    # 'city': 'Gwenborough',
    # 'zipcode': '92998-3874',
    # }
}
print(users)
# Untuk memnaggil dictionary tertentu
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
# print(users["address"][street])

print(users)
print(type(users))
print("\nUbah Dictionary ke JSON")
result = json.dumps(users)
print(result)
print(type(result))

with open('result.json', 'w') as file:
    json.dump(users, file)
