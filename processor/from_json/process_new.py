import json

# give the data type as 'raw' or 'reoriented'
type = 'raw'
# name of the file you want to edit
file_name = 'Bandaragama Road Weralugas Junction' # change accordingly
# list of timestamp for potholes
start_time = 1538357557818
# 1538359628951
pothole_array = [10291, 14512, 819112, 819917, 824752, 843832, 858533, 862233,
                 872992, 877913, 878712, 922412, 928653, 957692, 959593,
                 962212, 963312, 967933, 974153, 1047914, 1066613, 1073333, 1085292, 1090332,
                 1115552, 1126792, 1184872, 1213692, 1284712, 1286613, 1285912,
                 1305394, 1307112, 1318774, 1375612, 1388475, 1390092, 1447754,
                 1670953, 1998612, 2017793, 2028133, 2064313, 2071133, 2104192, 2113731,
                 2118151, 2176431, 2177931, 2190092]  # change accordingly
# list of timestamp for bumps
bump_array = [ 870272, 896193, 910075, 1201332, 1210173, 1329113, 1338656,
               2019091]  # change accordingly
# list of timestamp for speed breakers
speed_breaker_array = []  # change accordingly

count = 0
print(len(pothole_array)+len(bump_array))
with open('../../input/json/'+type+'/'+file_name+'.json') as data_file:
    file = json.load(data_file)
    print(len(file))
    #  initiate as no anomalies

    for element in file:
        current_anomaly = "N"
        time = float(element['time'])-start_time
        #  update if anomalies found
        if time in pothole_array:
            current_anomaly = "A"
            count = count +1
            # print(time)
        elif time in bump_array:
            current_anomaly = "A"
            count = count + 1
            # print(time)
        # else:
        #     current_anomaly = "N"
        element['anomaly'] = current_anomaly

    print(count)

    # file will be saved with the same name
    with open('../../output/from_json/'+type+'/'+file_name+'.json', 'w') as out_file:
        json.dump(file, out_file)
