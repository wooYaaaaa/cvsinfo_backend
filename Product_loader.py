import json

with open('C:/Users/82103/Desktop/cvsinfo_backend/Product.json', 'r', encoding='UTF-8') as f:
    products = json.load(f)

new_list = []
for product in products:
    new_data = {"model": "cvsinfo.product"}
    new_data["fields"] = product
    new_list.append(new_data)

with open('C:/Users/82103/Desktop/cvsinfo_backend/Product_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)