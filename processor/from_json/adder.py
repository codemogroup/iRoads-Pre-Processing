import json

# give the data type as 'raw' or 'reoriented'
type = 'raw'
# name of the file you want to edit
file_name = 'j7thalala7leftsidepothole2wheel' # change accordingly
# list of timestamp for potholes
pothole_array = []  # change accordingly
# list of timestamp for bumps
bump_array = []  # change accordingly
# list of timestamp for speed breakers
speed_breaker_array = []  # change accordingly
mainArray = None
array1 = None
with open('../../output/from_json/'+type+'/'+file_name+'.json') as data_file1:
    array1 = json.load(data_file1)

print(len(array1))
with open('../../output/TrainingData/'+'TrainingData.json') as data_file:
    mainArray = json.load(data_file)
print(len(mainArray))
startTime = mainArray[-1]["timeCount"] + 100
for item in array1:
    item["timeCount"] = item["time"] - array1[0]["time"] + startTime
    mainArray.append(item)
with open('../../output/TrainingData/'+'/'+'TrainingData.json', 'w') as out_file:
    json.dump(mainArray, out_file)

with open('../../output/TrainingData/'+'TrainingData.json') as data_file:
    mainArray = json.load(data_file)
    print(len(mainArray))


#
# with open('../../output/from_json/'+type+'/'+file_name+'.json') as data_file1:
#     array1 = json.load(data_file1)
#
# print(len(array1))
# for item in array1:
#     item["timeCount"] = item["time"] - array1[0]["time"]
# with open('../../output/TrainingData/'+'/'+'TrainingData.json', 'w') as out_file:
#     json.dump(array1, out_file)
#
# with open('../../output/TrainingData/'+'TrainingData.json') as data_file:
#     mainArray = json.load(data_file)
#     print(len(mainArray))