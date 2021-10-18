'''
    already know two access file idx
    make them to a new one, save it

    divide each file to 4 parts
    
'''
import os
import random

def single_offspring(parent1, parent2, offspring_id, root_path, batch_idx):

    length_1 = len(open(parent1, 'r').readlines())
    length_2 = len(open(parent2, 'r').readlines())

    offspring_data = []

    offspring = root_path + 'access_' + os.path.basename(parent1)[7:-4] +\
        '_' + os.path.basename(parent2)[7:-4] + '_' + str(offspring_id) +\
            '_' + str(batch_idx) + '.txt'

    if offspring_id == 1:

        # 0~1/2 + 0~1/2, named access_A_B_1.txt
        # A is parent1's idx, B is parent2's idx.
        with open(parent1, 'r') as par_1:
            for idx in range(int(length_1/2)):
                lane_id = par_1.readline()
                offspring_data.append(lane_id)
        
        with open(parent2, 'r') as par_2:
            for idx in range(int(length_2/2)):
                lane_id = par_2.readline()
                offspring_data.append(lane_id)

    elif offspring_id == 2:

        # 1/2~1 + 1/2~1, named access_A_B_2.txt
        # A is parent1's idx, B is parent2's idx.
        with open(parent1, 'r') as par_1:
            for idx in range(int(length_1/2), length_1):
                lane_id = par_1.readline()
                offspring_data.append(lane_id)
        
        with open(parent2, 'r') as par_2:
            for idx in range(int(length_2/2), length_2):
                lane_id = par_2.readline()
                offspring_data.append(lane_id)
    
    elif offspring_id == 3:
    
        # 0~1/2 + 1/2~1, named access_A_B_3.txt
        # A is parent1's idx, B is parent2's idx.
        with open(parent1, 'r') as par_1:
            for idx in range(int(length_1/2), length_1):
                lane_id = par_1.readline()
                offspring_data.append(lane_id)
        
        with open(parent2, 'r') as par_2:
            for idx in range(int(length_2/2), length_2):
                lane_id = par_2.readline()
                offspring_data.append(lane_id)
    
    elif offspring_id == 4:
    
        # 1/2~1 + 0~1/2, named access_A_B_4.txt
        # A is parent1's idx, B is parent2's idx.
        with open(parent1, 'r') as par_1:
            for idx in range(int(length_1/2), length_1):
                lane_id = par_1.readline()
                offspring_data.append(lane_id)
        
        with open(parent2, 'r') as par_2:
            for idx in range(int(length_2/2), length_2):
                lane_id = par_2.readline()
                offspring_data.append(lane_id)

    all_lane_num = len(offspring_data)

    # make 1% heteromorphosis and 5% missing and 2% add
    # update: make 5% heteromorphosis and 5% missing and 5% add
    change_num = max(1, int(0.1*all_lane_num))
    for idx in range(change_num):
        offspring_data[random.randint(0, all_lane_num-1)] = str(random.randint(0, 35188)) + '\n'
    missing_num = max(1, int(0.05*all_lane_num))
    for idx in range(missing_num):
        offspring_data[random.randint(0, all_lane_num-1)] = ''
    add_num = max(1, int(0.05*all_lane_num))
    for idx in range(add_num):
        offspring_data.append(str(random.randint(0, 35188)) + '\n')

    with open(offspring, 'w') as offsp:
        offsp.writelines(offspring_data)
    


# if __name__ == '__main__':
#     for i in range(4):
#         single_offspring('access1.txt', 'access10.txt', i + 1, './', 0)
    