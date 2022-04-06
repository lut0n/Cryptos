import json

with open('Log.json', 'r') as f:
    json_in = json.loads(f.read())
    f.close()
    json_in["Logs"] = []
json_dict = json.dumps(json_in, indent=1)
with open('Log.json', 'w') as f:
    f.write(json_dict)
    f.close()
print('Cleaned...')

