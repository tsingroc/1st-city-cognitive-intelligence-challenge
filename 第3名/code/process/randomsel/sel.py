
import sys
import random

def random_sel(in_file, out_file, sel_num):

    with open(in_file, 'r') as f:
        data = f.readlines()
        sel_data = random.sample(data, sel_num)
        with open(out_file, 'w') as out_file:
            out_file.writelines(sel_data)


if __name__ == '__main__':
    random_sel('all_correct.txt', sys.argv[1], int(sys.argv[2]))
    