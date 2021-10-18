echo "每次调用之前都+1"
echo "start GA, Now is 15"

i=$1

source activate torch140

cd /home/kaiyuecheng/data/disk2T/kaiyuec_data/data/czcompetition
./moveold.sh $i

cd /home/kaiyuecheng/competition/cz/process/ga
python currdata.py $i

((i++))

./run.sh $i

htop