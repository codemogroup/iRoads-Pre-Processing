import json
import math



def getDistance(lon1, lat1, lon2, lat2):
    # print()
    r = 6371000
    phi1 = getRadiant(lat1)
    phi2 = getRadiant(lat2)
    deltaPhi = getRadiant(lat2 - lat1)
    deltaLamda = getRadiant(lon2 - lon1)
    a = math.sin(deltaPhi / 2.0) * math.sin(deltaPhi / 2.0) + math.cos(phi1) * math.cos(phi2) * math.sin(deltaLamda / 2.0) * math.sin(deltaLamda / 2.0)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    meters = r * c
    km = meters / 1000.0
    # print(lon1, lat1, lon2, lat2, km)
    return km


def getRadiant(degree):
    radiant = degree * (2 * math.pi / 360)
    return radiant


start = False


def calcSpeed(lon1, lat1, lon2, lat2, time1, time2):
    distance = getDistance(lon1, lat1, lon2, lat2)
    timeDiff = (time2 - time1) / 3600000
    # print(timeDiff)
    speed = distance / timeDiff
    return speed

print("start")
with open('../../input/txt/raw/j5_tida_sirini1.txt', 'r') as myfile:
    data = myfile.read()
    data_array = data.split("},{")
    newData = []
    for k in range(len(data_array)):
        newItem = {}
        item_object = data_array[k].split(",")


        newItem["lon"] = item_object[1].split("=")[1]
        newItem["acceY"] = item_object[2].split("=")[1]
        newItem["acceY_raw"] = item_object[3].split("=")[1]
        newItem["time"] = int(item_object[4].split("=")[1])
        # print(newItem["time"])
        newItem["acceX"] = item_object[5].split("=")[1]
        newItem["obdRpm"] = item_object[6].split("=")[1]
        newItem["imei"] = item_object[7].split("=")[1]
        # newItem["gpsSpeed"] = item_object[8].split("=")[1]
        # newItem["journeyID"] = item_object[9].split("=")[1]
        newItem["journeyID"] = item_object[8].split("=")[1]
        # newItem["obdSpeed"] = item_object[10].split("=")[1]
        newItem["obdSpeed"] = item_object[9].split("=")[1]
        # newItem["acceZ_raw"] = item_object[11].split("=")[1]
        newItem["acceZ_raw"] = item_object[10].split("=")[1]
        # newItem["dataType"] = item_object[13].split("=")[1]
        newItem["dataType"] = item_object[12].split("=")[1]
        # newItem["lat"] = item_object[14].split("=")[1]
        newItem["lat"] = item_object[13].split("=")[1]
        # newItem["acceX_raw"] = item_object[15].split("=")[1]
        newItem["acceX_raw"] = item_object[14].split("=")[1]
        # newItem["acceZ"] = item_object[16].split("=")[1]
        newItem["acceZ"] = item_object[15].split("=")[1]

        newData.append(newItem)

    # data1 = json.loads(input, encoding='utf-8')

    newData = sorted(newData,key = lambda x : x["time"])
    print("1111111111111111111111111111111111111111111111")
    for item in newData:
        print(item["time"])

    print("22222222222222222222222222222222222222222222")
    newDataSet = []
    loc_changed = False
    last_lon = 0.0
    last_lat = 0.0
    last_time = 0.0
    last_speed = 0.0
    for k in range(len(newData)):

        if k != 0:
            lon = float(newData[k]["lon"])
            lat = float(newData[k]["lat"])
            time = int(newData[k]["time"])
            if not (last_lat == lat and last_lon == lon):
                newData[k]["gpsSpeed"] = calcSpeed(last_lon, last_lat, lon, lat, last_time, time)
            else:
                newData[k]["gpsSpeed"] = last_speed
        else:
            newData[k]["gpsSpeed"] = 0.0
            last_lon = float(newData[k]["lon"])
            last_lat = float(newData[k]["lat"])
            last_time = int(newData[k]["time"])

        # print(newItem["gpsSpeed"])

            # newData.append(newItem)

    print("3333333333333333333333333333333333333333333333333333")
    for item in newData:
        print(item["gpsSpeed"])

    print("Length    : " + str(len(data_array)))
    print(data_array[0])



with open('../../output/from_txt/raw/j5_tida_sirini1.json', 'w', encoding='utf8') as outfile:
    json.dump(newData, outfile, ensure_ascii=False, indent=4)

print("end")


# print("start")
# with open('loguwin_last .txt', 'r') as myfile:
#     input = myfile.read().replace('\n', '')
#     data1 = json.loads(input, encoding='utf-8')
#     print("Length    : " + str(len(data1)))
#     redirects = {}
#     for p in range(len(data1)):
#         # print('Title: ' + p['title'])
#         print(str(p))
#         redirects[data1[p]['redirect']] = None,
# 
#     print("Total redirects    : "+str(len(redirects)))
#     for p in range(len(data1)):
#         redirects[data1[p]['redirect']] = redirects[data1[p]['redirect']] + (data1[p]['title'],)
# 
#     newData = []
#     for key, value in redirects.items():
#         item = {}
#         item["redirect"] = key
#         item["titles"]=[]
#         for title in value:
#             if title is not None:
#                 item["titles"] = item["titles"]+[title]
#         newData.append(item)
# 
#     with open('datanew.json', 'w', encoding='utf8') as outfile:
#             json.dump(newData, outfile, ensure_ascii=False, indent=4)
# 
# print("end")
