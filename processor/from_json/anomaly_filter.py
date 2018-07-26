import json

# give the data type as 'raw' or 'reoriented'
type = 'classified'
# name of the file you want to edit
file_name = 'j7Uduwila1PotholeModel' # change accordingly

with open('../../input/json/'+type+'/'+file_name+'.json') as data_file:
    file = json.load(data_file)
    print(len(file))
    # list of anomalies found
    anomaly_array = []
    for element in file:
        anomaly = element['anomaly']
        #  update if anomalies found
        if anomaly != "N":
            anomaly_array.append(element)

    # file will be saved with the same name
    with open('../../output/from_json/'+type+'/'+file_name+'.json', 'w') as out_file:
        json.dump(anomaly_array, out_file)
