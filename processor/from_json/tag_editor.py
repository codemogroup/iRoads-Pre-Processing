import json

# give the data type as 'raw' or 'reoriented'
type = 'manual_tags'
# name of the file you want to edit
file_name = 'Bandaragama Road Weralugas Junction' # change accordingly
start_time = 1538357557818


def sort_by_time(t):
    return t['chart_time']


with open('../../input/json/'+type+'/'+file_name+'.json') as data_file:
    file = json.load(data_file)
    print(len(file))

    for element in file:
        time = float(element['time'])-start_time

        element['chart_time'] = time

    file = sorted(file, key=sort_by_time)

    # file will be saved with the same name
    with open('../../output/from_json/'+type+'/'+file_name+'.json', 'w') as out_file:
        json.dump(file, out_file)
