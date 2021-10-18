import json

MAP_FILE = "../../data/map.json"

def all_correct(mapfile, outfile):

    with open(outfile, 'w') as out_file:
        out_file.write("all correct\n")

    with open(mapfile, 'r') as map_file:
        map_data = json.load(map_file)

    map_idx = 1

    with open(outfile, 'a+') as out_file:
        while map_data[map_idx]["class"] == "lane":
            if not\
                (map_data[map_idx]["data"]["successor_ids"] == []\
                and map_data[map_idx]["data"]["predecessor_ids"] == [])\
                :
                out_file.write(str(map_data[map_idx]["data"]["id"]) + "\n")
                # out_file.write("\n")
            # print(map_data[1]["data"]["predecessor_ids"])
            # print(map_data[1]["class"])
            if map_idx % 1000 == 0:
                print(map_idx)
            map_idx += 1



if __name__ == '__main__':
    all_correct(MAP_FILE, './all_correct.txt')