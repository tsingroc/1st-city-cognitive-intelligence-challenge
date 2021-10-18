'''
    This is GA arithmetic code.
    First, we get the top 40 of current result access.
    We write the arithmetic in this python file,
    and write the loop in a bash file.

    We use while True to make it run all the time,
    when we get the result we want, we stop it.
'''

import os
import sys
import random

from single import single_offspring

def ga_arithmetic(root_path, target_path):

    if not os.path.exists(target_path):
        os.mkdir(target_path)

    # make a 1 to 40 random list
    for batch_id in range(2):
        all_access = [i for i in range(1, 41)]
        random.shuffle(all_access)
        parent_list = [(all_access[i], all_access[39-i]) for i in range(20)]
        for parents in parent_list:
            parent1 = root_path + 'access_' + str(parents[0]) + '.txt'
            parent2 = root_path + 'access_' + str(parents[1]) + '.txt'
            for offspring_id in range(4):
                single_offspring(parent1, parent2, offspring_id + 1, target_path, batch_id)

def rename_access(access_path):

    access_list = os.listdir(access_path)
    access_idx = 1
    for access_file in access_list:
        if access_file[-4:] == '.txt':
            # print(access_file)
            old_name = os.path.join(access_path, access_file)
            new_name = os.path.join(access_path, 'access_' + str(access_idx) + '.txt')
            os.rename(old_name, new_name)
            access_idx += 1

if __name__ == '__main__':
    rename_access(sys.argv[1])
    ga_arithmetic(sys.argv[1], sys.argv[2])
    rename_access(sys.argv[2])
    

