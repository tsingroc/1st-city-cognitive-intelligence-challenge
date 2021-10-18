
from collections import Counter



def get_car(path):

    bad_lane = []
    for curr_data in open(path, 'r'):
        # 2, 5, 8, ..., 3n+2, ...
        data_list = str.split(curr_data)
        
        if len(data_list) == 1:
            continue
        select = list(range(len(data_list)))[2::3]
        
        result = Counter(data_list[2::3])
        sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        for result in sorted_result:
            if result[1] >= 100 and result[0] not in bad_lane:
                bad_lane.append(result[0])

    print(bad_lane)
    
    pass



if __name__ == '__main__':
    get_car('./out720/traj.txt')
    