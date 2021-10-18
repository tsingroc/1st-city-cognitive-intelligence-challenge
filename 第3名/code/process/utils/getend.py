import json

MAP_FILE = "../../data/map.json"

def get_end(mapfile, outfile):

    with open(mapfile, 'r') as map_file:
        map_data = json.load(map_file)

    print(map_data[1]["data"]["predecessor_ids"])
    print(map_data[1]["class"])