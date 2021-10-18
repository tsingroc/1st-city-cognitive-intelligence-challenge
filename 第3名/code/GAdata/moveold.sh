
time=$(date "+%Y_%m_%d_%H_%M_%S")
echo $time

mkdir raw_data/$time

cp -r gadata/epoch$1 raw_data/$time/
cp -r gadata/resultlist$1 raw_data/$time/

# rename
mv raw_data/$time/epoch$1/ raw_data/$time/accesslist/
mv raw_data/$time/resultlist$1/ raw_data/$time/resultlist/
# mkdir accesslist
# mkdir resultlist