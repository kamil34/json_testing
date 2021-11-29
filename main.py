import json

def save_json():
    data = {}
    data['record'] = []
    data['record'].append({
        'username': 'test1',
        'domain': 'test1.local',
        'phone': '+1 212 456 7890',
        'email_address': 'test1@admin.local'
    })
    data['record'].append({
        'username': 'test2',
        'domain': 'test2.local',
        'phone': '+1 212 456 7891',
        'email_address': 'test2@admin.local'
    })
    with open('data.json', 'w') as json_file:
        try:
            json.dump(data, json_file, indent=4, sort_keys=True)
        except KeyError as err:
            print('A KeyError occurred!\n', err)
        else:
            print('done saving')

# use the line below in case you need to make json dump
# save_json()

def load_json():
    with open('data.json', 'r') as json_file:
        data = {}
        data = json.load(json_file)
        print(data['record'])
        print(len(data['record']))
        for i in range(0, len(data['record'])):
            print(data['record'][i])

load_json()