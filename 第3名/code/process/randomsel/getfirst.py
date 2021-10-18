
import os

def get_rank1_id(result_path):
    
    dir_list = os.listdir(result_path)
    score_list = []

    for dir_path in dir_list:

        time_file = os.path.join(result_path, dir_path, "time.txt")
        if os.path.exists(time_file):
            with open(time_file, 'r') as f:
                score = f.readline()
            if score == "":
                continue
            score_list.append([int(dir_path[4:]), float(score[:-1])])

    score_list.sort(key=lambda x:x[1])
    print("rate of progress " + str(len(dir_list)) + '/' + "1000")
    print("Rank 1:", score_list[0])
    output_score_list(score_list)
    

def output_score_list(score_list):
    
    print('-'*25+"\n|\tScore list\t|\n"+'-'*25)
    print("|rank\t|id\t|score\t|\n"+'-'*25)
    for idx in range(min(len(score_list), 30)):
        score_str = str(score_list[idx][1])
        if len(str(score_list[idx][1])) > 6:
            score_str = str(score_list[idx][1])[:6]
        print("|"+str(idx+1)+"\t|"+str(score_list[idx][0])+\
            "\t|"+score_str+"\t|")
    print('-'*25)



if __name__ == '__main__':
    try:
        get_rank1_id("./resultlist")
    except:
        print("There is something wrong.")
    