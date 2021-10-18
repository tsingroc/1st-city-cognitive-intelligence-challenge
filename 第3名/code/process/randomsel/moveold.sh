
time=$(date "+%Y_%m_%d_%H_%M_%S")
echo $time

mkdir $time

mv accesslist $time
mv resultlist $time

mkdir accesslist
mkdir resultlist