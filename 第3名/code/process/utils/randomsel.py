
import random

def random_sel(in_file, out_file):

    with open(in_file, 'r') as f:
        data = f.readlines()
        sel_data = random.sample(data,1000)
        # print(sel_data)
        with open(out_file, 'w') as out_file:
            out_file.writelines(sel_data)


if __name__ == '__main__':
    random_sel('only_fast.txt', 'out.txt')
    