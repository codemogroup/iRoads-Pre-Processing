import json

# give the data type as 'raw' or 'reoriented'
type = 'raw'
# name of the file you want to edit
file_name = 'bump' # change accordingly
# list of timestamp for potholes
pothole_array = []  # change accordingly
# list of timestamp for bumps
bump_array = [1529838293132, 1529838293213,  1529838293312,1529838293412,  1529838293512,  1529838293612,  1529838293732,  1529838293832, 1529838293951,
              1529838294019,1529838294154,  1529838294214,  1529838294332,1529838294432,  1529838294532,  1529838294632,  1529838294753, 1529838294834,
              1529838294932]  # change accordingly
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
