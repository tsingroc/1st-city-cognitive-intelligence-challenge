
echo "start"

./ga_init.sh $[$1-1]
sleep 10s
nohup ./run_ga1.sh $1 &
sleep 10s
nohup ./run_ga2.sh $1 &
sleep 10s
nohup ./run_ga3.sh $1 &
sleep 10s
nohup ./run_ga4.sh $1 &
sleep 10s
nohup ./run_ga5.sh $1 &
sleep 10s
nohup ./run_ga6.sh $1 &
sleep 10s
nohup ./run_ga7.sh $1 &
sleep 10s
nohup ./run_ga8.sh $1 &
sleep 10s
nohup ./run_ga9.sh $1 &
sleep 10s
nohup ./run_ga10.sh $1 &
sleep 10s
nohup ./run_ga11.sh $1 &
sleep 10s
nohup ./run_ga12.sh $1 &
sleep 10s
nohup ./run_ga13.sh $1 &
sleep 10s
nohup ./run_ga14.sh $1 &
sleep 10s
nohup ./run_ga15.sh $1 &
sleep 10s
nohup ./run_ga16.sh $1 &
# ./ga_init.sh
# ./run_ga1.sh
# ./run_ga2.sh
# ./run_ga3.sh
# ./run_ga4.sh

echo "done"