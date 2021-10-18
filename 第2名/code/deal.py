import json


def throughput(rl, bl, ol, tj):  # throughput(堵的道,路口道,上条道,交通数据)
    dic1 = dict() # 生成空字典
    thruput = 0 # 表示“上条道”对“堵的道”的车流贡献量
    for i in range(90, 270): # 在观测的30分钟内
        data = list(tj[i].split()) # 读取某一时刻的车辆信息
        cnt = len(data)
        for j in range(1, cnt, 3): # 对每一辆车进行观察
            if data[j + 1] == ol: # 如果该车在“上条道”上
                dic1[data[j]] = data[j + 1] # 则将该车计入字典

        data = list(tj[i + 1].split()) # 读取下一时刻的车辆信息
        cnt = len(data)
        for j in range(1, cnt, 3): # 再观察每一辆车
            if data[j] in dic1: # 如果这辆车在上一时刻在“上条道”上
                if data[j + 1] == rl or data[j + 1] == bl: # 且这一时刻在“堵的道”或“路口道”上
                    thruput = thruput + 1 # 则该车属于“上条道”对“堵的道”贡献的车流
        dic1.clear() # 清空字典供下次循环使用
    return thruput # 输出贡献量

'''上面的throughput函数用于计算“上条道”对“堵的道”的车流贡献量，即前文所提的第三部分。
核心思路就是寻找上一时刻在“上条道”、下一时刻在“堵的道”或“路口道”上的车辆并计数'''

def getLaneLink(lane_id, Lane2predec):  # 输入参数为目标车道以及前驱车道列表
    Linklist = []
    for info in Lane2predec[lane_id]:
        if Lane2predec[info] == []:  # 如果前驱的前驱为空则跳过
            continue
        templist = []
        templist.append(lane_id)
        templist.append(info)  # 前驱车道id
        templist.append(Lane2predec[info][0])  # 前驱的前驱车道id
        Linklist.append(templist)
    return [Linklist]

'''这个getLaneLink函数用于寻找目标车道之前的车道，即前文中的第二部分。
核心思路就是遍历所有车道，查找其前驱车道及前驱车道的前驱车道，
值得注意的是一条车道可能有多组前驱车道及前驱车道的前驱车道'''

with open('map.json', 'r', encoding='utf8') as fp: # 读取道路信息文件
    json_data = json.load(fp)
header = json_data[0]
laneList = [] # 车道列表
roadList = [] # 道路列表
junctionList = [] # 路口列表
poiList = [] # 兴趣点列表
for info in json_data:
    if info.get('class') == 'lane': # 如果类型是“车道”
        laneList.append(info.get('data')) # 则将该车道信息计入车道列表，下面三个同理
    elif info.get('class') == 'road':
        roadList.append(info.get('data'))
    elif info.get('class') == 'junction':
        junctionList.append(info.get('data'))
    elif info.get('class') == 'poi':
        poiList.append(info.get('data'))

'''以上部分是将车道、道路、路口和兴趣点的信息整理成列表以便于后续的查阅'''

lane2parent = {}  # 标记所属的路口id或路id
lane2predec = {}  # predecessorid  前驱车道字典
lane2succes = {}  # successorid    后继车道字典
lane2junc = {}  # 获得某车道 相连的路口
 # Lane2parent、lane2predec、lane2succes通过线性遍历laneList列表进行赋值。
for info in laneList:
    lane2parent[info.get('id')] = info.get('parent_id')
    lane2predec[info.get('id')] = info.get('predecessor_ids')
    lane2succes[info.get('id')] = info.get('successor_ids')
for info in laneList:
    # ane2juc(value为key车道id相连的路口，如果属于路口，则为单值，即路口id；如果属于路，则元素为列表，列表第一个元素为前驱的路口id，第二个元素为后继的路口id)
    if info.get('parent_id') > 300000000:  # 区分车道属于路口还是属于路在于parent_id首位数字，首位为2代表属于路，首位为3代表属于路口
        lane2junc[info.get('id')] = info.get('parent_id')
    else:  # 如果车道不属于路口，则找到该车道的上一个路口和下一个路口 实现过程中发现，其前驱后继均属于路口。即一条车道若属于路，其前驱后继(若存在)均属于路口。 
        b = lane2predec[info.get('id')]  # 获得前继列表
        prejunc = []
        for a in b:
            if lane2parent[a] > 300000000: #若属于路口
                prejunc.append(lane2parent[a])
            else:
                prejunc.append('0') # 用来观察是否存在特殊情况 实现中发现并不存在
        b = lane2succes[info.get('id')]  # 获得后继列表
        sucjunc = []
        for a in b:
            if lane2parent[a] > 300000000: #若属于路口
                sucjunc.append(lane2parent[a])
            else:
                sucjunc.append('0')
        lane2junc[info.get('id')] = {'pre': prejunc, 'suc': sucjunc}

'''以上部分是将车道信息进一步整理，得到关于车道前后连接、与路口连接等信息的字典，便于后面的查阅'''

print("finish reading road info")

with open('traj.txt', 'r') as f: # 读取车辆行驶数据
    tj = f.readlines()

dic_poi = dict() # 以有兴趣点的车道id为索引的字典，内容为兴趣点在该车道上的位置。用于查阅哪些车道上有兴趣点

for i in poiList:
    i['driving_position']['lane_id']
    dic_poi[str(i['driving_position']['lane_id'])] = tuple(
        dic_poi.get(str(i['driving_position']['lane_id']), "n")) + tuple(
            [i['driving_position']['s']]) # 遍历所有兴趣点，以所在车道id为索引、所在位置为内容记录

'''以上部分是在整理兴趣点信息，得到拥有兴趣点的车道的信息'''

# d = float(data1[0])
dic1 = dict() # 两个用于记录相邻两时刻车辆信息的字典
dic2 = dict()
dic_lane = dict() # 记录拥堵车道的字典：索引为拥堵车道的id，内容为汽车拥堵的位置
threshold = 1 # 判断车辆是否拥堵的速度阈值
distance = 0 # 用于记录车辆移动距离

for i in range(90, 270): # 在观测的30分钟内
    data = list(tj[i].split()) # 读取某一时刻车辆行驶信息
    cnt = len(data)
    for j in range(1, cnt, 3): # 遍历该时刻的每一辆车
        dic1[data[j]] = (data[j + 1], float(data[j + 2])) # 以车辆id为索引，记录所在车道及位置

    data = list(tj[i + 1].split()) # 读取下一时刻车辆行驶信息
    cnt = len(data)
    for j in range(1, cnt, 3): # 遍历每一辆车
        dic2[data[j]] = (data[j + 1], float(data[j + 2])) # 记录车辆id、位置
        if data[j] in dic1: # 如果该车在上一时刻仍在路网中
            if dic1[data[j]][0] == dic2[data[j]][0]: # 且上一时刻与当前时刻在同一车道上
                distance = dic2[data[j]][1] - dic1[data[j]][1] # 则计算这段时间内的行驶距离
                if distance < threshold: # 如果行驶距离小于阈值
                    dic_lane[data[j + 1]] = tuple(
                        dic_lane.get(data[j + 1], "n")) + tuple(
                            [float(data[j + 2])]) # 则判定该车已被堵住，将其所在车道及位置计入拥堵车道字典
    dic1.clear()
    dic2.clear() # 清空字典供下次循环使用

'''以上部分是在分析当前的交通状况，提取出拥堵车道的id，即前文中的第二部分。
核心思路为同时读取相邻两时刻的车辆行驶信息，寻找两个时刻都在同一车道的车，
计算其移动距离，与阈值比较、记录。'''

print('finish analyzing traj')
Acc = open("access.txt", "w+") # 打开记录文件

for jamlane in dic_lane.keys(): # 遍历每一条拥堵车道
    prelaneList = getLaneLink(int(jamlane), lane2predec) # 用getLaneLink函数得出拥堵车道的前驱车道及前驱车道的前驱车道
    maxIndex = 0 # 记录对拥堵车道车流量贡献最大的前驱车道的id
    maxThroughput = 0 # 单条前驱车道对拥堵车道车流贡献量的最大值
    for prelanei in prelaneList[0]: # 遍历每一条前驱车道及前驱车道的前驱车道
        if str(prelanei) in dic_poi: # 如果前驱车道上有兴趣点
            continue # 则忽视后面的判断，因为有兴趣点的车道不能删
        currentThroughput = throughput(str(prelanei[0]), str(prelanei[1]), str(prelanei[2]), tj) # 用throughput函数计算各前驱车道的前驱车道对拥堵车道的车流贡献量
        if currentThroughput > maxThroughput:
            maxIndex = prelanei[2]
            maxThroughput = currentThroughput # 记录车流贡献量最大的车道id及贡献量
    Acc.write(str(maxIndex)) # 将车流贡献量最大的车道id计入文件
    Acc.write('\n') # 转行
Acc.close() # 关闭记录文件

'''以上部分是在整合之前各部分的功能，得到待删目录，即第四部分的主要功能。
思路是寻找对每一条拥堵车道车流量贡献最大的车道，将该车道id计入待删目录'''