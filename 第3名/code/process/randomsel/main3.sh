
echo "start random sel..."

ALL_NUM=10000

for ((i=1; i<=$ALL_NUM; i++))
do
    if [ $[$i%4] -eq 3 ];
    then
        echo start $i/$ALL_NUM
        # get access.txt
        ACCESS_PATH=/home/kaiyuecheng/data/disk2T/kaiyuec_data/data/czcompetition/accesslist/access_$i.txt
        python sel.py $ACCESS_PATH $[$RANDOM%400+1]

        # get output path
        OUT_PATH=/home/kaiyuecheng/data/disk2T/kaiyuec_data/data/czcompetition/resultlist/out_$i
        mkdir $OUT_PATH

        # run
        sudo docker run --mount type=bind,source=$OUT_PATH,target=/output \
        --mount type=bind,source=$ACCESS_PATH,target=/access.txt \
        --rm git.tsingroc.com:5050/release/cup2109:latest
    fi
    
done
