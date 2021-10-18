
echo "start GA Init..."

source activate torch140

# get access list from last epoch
RAW_PATH=/home/kaiyuecheng/data/disk2T/kaiyuec_data/data/czcompetition/gadata/epoch$1p/
ACCESS_LIST=/home/kaiyuecheng/data/disk2T/kaiyuec_data/data/czcompetition/gadata/epoch$[$1+1]/
mkdir /home/kaiyuecheng/data/disk2T/kaiyuec_data/data/czcompetition/gadata/resultlist$[$1+1]/
python ga.py $RAW_PATH $ACCESS_LIST
