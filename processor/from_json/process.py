import json

# give the data type as 'raw' or 'reoriented'
type = 'raw'
# name of the file you want to edit
file_name = 'pothole_40kmph' # change accordingly
# list of timestamp for potholes
pothole_array = [1529838251642, 1529838251742, 1529838251842,
1529838251942,1529838252050,1529838252159,
1529838252247, 1529838252348, 1529838252447,
1529838252562, 1529838252651, 1529838252762,
1529838252852]  # change accordingly
# list of timestamp for bumps
bump_array = []  # change accordingly
# list of timestamp for speed breakers
speed_breaker_array = []  # change accordingly


with open('../../input/json/'+type+'/'+file_name+'.json') as data_file:
    file = json.load(data_file)
    print(len(file))
    for element in file:
        time = element['time']
        #  initiate as no anomalies
        element['anomaly'] = "N"
        #element['bump'] = 0
        #element['speed_breaker'] = 0
        #  update if anomalies found
        if time in pothole_array:
            element['anomaly']  = "P"
        elif time in bump_array:
            element['anomaly'] = "B"
        elif time in speed_breaker_array:
            element['anomaly'] = "S"

    # file will be saved with the same name
    with open('../../output/from_json/'+type+'/'+file_name+'.json', 'w') as out_file:
        json.dump(file, out_file)
