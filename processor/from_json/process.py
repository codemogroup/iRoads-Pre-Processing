import json

# give the data type as 'raw' or 'reoriented'
type = 'raw'
# name of the file you want to edit
file_name = 'j7uduwila1' # change accordingly
# list of timestamp for potholes
pothole_array = [1530858189559, 1530858190359, 1530858194360, 1530858195359, 1530858205179, 1530858205979, 1530858216399, 1530858217099, 1530858220607, 1530858222019, 1530858232136, 1530858233140, 1530858267293, 1530858267900]  # change accordingly
# list of timestamp for bumps
bump_array = []  # change accordingly
# list of timestamp for speed breakers
speed_breaker_array = []  # change accordingly


with open('../../input/json/'+type+'/'+file_name+'.json') as data_file:
    file = json.load(data_file)
    print(len(file))
    #  initiate as no anomalies
    current_anomaly = "N"
    anomaly_started = False
    for element in file:
        time = element['time']
        #  update if anomalies found
        if time in pothole_array:
            if anomaly_started:
                anomaly_started = False
                current_anomaly = "N"
            else:
                anomaly_started = True
                current_anomaly = "P"
        elif time in bump_array:
            if anomaly_started:
                anomaly_started = False
                current_anomaly = "N"
            else:
                anomaly_started = True
                current_anomaly = "B"
        elif time in speed_breaker_array:
            if anomaly_started:
                anomaly_started = False
                current_anomaly = "N"
            else:
                anomaly_started = True
                current_anomaly = "S"
        element['anomaly'] = current_anomaly

    # file will be saved with the same name
    with open('../../output/from_json/'+type+'/'+file_name+'.json', 'w') as out_file:
        json.dump(file, out_file)
