
import os

def get_rank1_id(result_path):
    
    experiment_list = os.listdir(result_path)
    
    score_list = []

    for experiment in experiment_list:
        
        dir_list = os.listdir(os.path.join(result_path, experiment, "resultlist"))
        # access_list = os.listdir(os.path.join(result_path, experiment, "accesslist"))
        
        for dir_path in dir_list:
            
            time_file = os.path.join(result_path, experiment, "resultlist", dir_path, "time.txt")
            access_file = os.path.join(result_path, experiment, "accesslist", "access_"+dir_path[4:]+".txt")
            if os.path.exists(time_file):
                with open(time_file, 'r') as f:
                    score = f.readline()
                access_length = len(open(access_file, 'r').readlines())
                if score == "":
                    continue
                score_list.append([int(dir_path[4:]), float(score[:-1]), int(access_length)])
                
    score_list.sort(key=lambda x:x[1])
    print("all num is {}".format(len(score_list)))
    # print("rate of progress " + str(curr_num) + '/' + "1000")
    # print("Rank 1:", score_list[0])
    output_score_list(score_list)
    

def output_score_list(score_list):
    
    print('-'*33+"\n|\t   Score list\t\t|\n"+'-'*33)
    print("|rank\t|id\t|score\t|length\t|\n"+'-'*33)
    for idx in range(min(len(score_list), 40)):
        score_str = str(score_list[idx][1])
        if len(str(score_list[idx][1])) > 6:
            score_str = str(score_list[idx][1])[:6]
        print("|"+str(idx+1)+"\t|"+str(score_list[idx][0])+\
            "\t|"+score_str+\
            "\t|"+str(score_list[idx][2])+"\t|")
    print('-'*33)



if __name__ == '__main__':
    # try:
    #     get_rank1_id("./raw_data")
    # except:
    #     print("There is something wrong.")
    get_rank1_id("./raw_data")
    