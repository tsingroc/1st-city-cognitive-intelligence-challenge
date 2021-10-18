
for ((i=1; i<=160; i++))
do
    if [ $[$i%16] -eq 4 ];
    then
    ACCESS_PATH=/home/kaiyuecheng/data/disk2T/kaiyuec_data/data/czcompetition/gadata/epoch$1/access_$i.txt
    echo $ACCESS_PATH

    # get output path
    OUT_PATH=/home/kaiyuecheng/data/disk2T/kaiyuec_data/data/czcompetition/gadata/resultlist$1/out_$i
    mkdir $OUT_PATH

    # run
    sudo docker run --mount type=bind,source=$OUT_PATH,target=/output \
    --mount type=bind,source=$ACCESS_PATH,target=/access.txt \
    --rm git.tsingroc.com:5050/release/cup2109:latest
    fi
done