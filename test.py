import json
from config import goods_photo

with open('messages.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
data_keys = data.keys()

print(type(data_keys))
print(data_keys)

goods_photo_keys = goods_photo.keys()
print(type(goods_photo_keys))
print(goods_photo.values())