import json
json_data = []

with open("funfact.txt","r") as filenames:
    for f in filenames:
        json_data.append(f.strip('\n')[2:])

    with open("funfact.json","w") as funfact:
        json.dump(json_data,funfact)