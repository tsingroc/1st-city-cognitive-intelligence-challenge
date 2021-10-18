time sudo docker run --mount type=bind,source=/home/kaiyuecheng/competition/cz/process/draw/out720,target=/output \
 --mount type=bind,source=/home/kaiyuecheng/competition/cz/process/draw/720.txt,target=/access.txt \
 --rm git.tsingroc.com:5050/release/cup2109:latest