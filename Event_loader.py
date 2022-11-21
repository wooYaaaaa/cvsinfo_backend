import json

with open('C:/Users/82103/Desktop/cvsinfo_backend/Event.json', 'r', encoding='UTF-8') as f:
    events = json.load(f)

new_list = []
for event in events:
    new_data = {"model": "cvsinfo.event"}
    new_data["fields"] = event
    new_list.append(new_data)

with open('C:/Users/82103/Desktop/cvsinfo_backend/Event_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)