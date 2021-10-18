import json

MAP_FILE = "../../data/map.json"

def get_left(mapfile, outfile):

    with open(outfile, 'w') as out_file:
        out_file.write("turn_left\n")

    with open(mapfile, 'r') as map_file:
        map_data = json.load(map_file)

    map_idx = 1

    with open(outfile, 'a+') as out_file:
        while map_data[map_idx]["class"] == "lane":
            if map_data[map_idx]["data"]["turn"] == "LANE_TURN_LEFT" \
                and map_data[map_idx]["data"]["successor_ids"] != []\
                and map_data[map_idx]["data"]["predecessor_ids"] != []\
                :
                out_file.write(str(map_data[map_idx]["data"]["id"]) + "\n")
                # out_file.write("\n")
            # print(map_data[1]["data"]["predecessor_ids"])
            # print(map_data[1]["class"])
            if map_idx % 1000 == 0:
                print(map_idx)
            map_idx += 1



if __name__ == '__main__':
    get_left(MAP_FILE, './turn_left.txt')