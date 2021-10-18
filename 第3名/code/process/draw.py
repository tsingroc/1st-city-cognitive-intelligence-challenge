import json
from os import access
import pyproj
import matplotlib.pyplot as plt
from tqdm import tqdm
import random

MAP_FILE = "../data/map.json"
NORTH = 4424461.667386686
SOUTH = 4409455.264332792
WEST = 440484.64473851764
EAST = 455890.8705902761
BAD_LIST = ['13359', '336', '4468', '4819', '4792', '7802']

ACCESS_FILE = './draw/720.txt'


def draw():
    flag = 'normal'
    plt.figure(figsize=(50, 50))
    with open(MAP_FILE, 'r') as map_file:
        map_data = json.load(map_file)

    with open(ACCESS_FILE, 'r') as access_file:
        access_data = str.split(access_file.read())

    
    for lane_idx in tqdm(range(35189)):

        draw_x = []
        draw_y = []
        try:
            for node_idx in range(len(map_data[lane_idx]["data"]["center_line"]["nodes"])):
                draw_x.append(map_data[lane_idx]["data"]["center_line"]["nodes"][node_idx]["x"] - WEST)
                draw_y.append(map_data[lane_idx]["data"]["center_line"]["nodes"][node_idx]["y"] - SOUTH)
            if str(lane_idx) in BAD_LIST:
                flag = 'bad'
                plt.plot(draw_x, draw_y, linewidth=1, color='r')
            elif str(lane_idx) in access_data:
                flag = 'access'
                plt.plot(draw_x, draw_y, linewidth=1, color='g')
            else:
                plt.plot(draw_x, draw_y, linewidth=0.1, color='k')
        except:
            continue
        if flag != 'normal':
            flag = 'normal'
            point_num = len(draw_x)
            if point_num > 2:
                draw_id = random.randint(0, point_num-1)
                plt.text(x=draw_x[draw_id],
                        y=draw_y[draw_id],
                        s=lane_idx,
                        rotation=1,
                        ha='left',
                        va='baseline',
                        fontdict=dict(fontsize=3, color='k',
                                    family='monospace',
                                    weight='light',
                                    
                                    )
            )
            else:
                rate = random.random()
                plt.text(x=draw_x[0]+rate*(draw_x[1]-draw_x[0]),
                        y=draw_y[0]+rate*(draw_y[1]-draw_y[0]),
                        s=lane_idx,
                        rotation=1,
                        ha='left',
                        va='baseline',
                        fontdict=dict(fontsize=3, color='k',
                                    family='monospace',
                                    weight='light',
                                    
                                    )
            )
    
    
    # plt.show()
    plt.savefig('./demo14.png', dpi=300)
    print('done')

if __name__ == '__main__':
    draw()