import json
import csv

with open('Scrapped_Data_MCF.json') as json_file:
    data = json.load(json_file)

with open('Scrapped_Data_MJG.json') as json_file:
    data2 = json.load(json_file)
    data.update(data2)

with open('Scrapped_Data_AGV.json') as json_file:
    data3 = json.load(json_file)
    data.update(data3)

with open('Scrapped_Data_ZYL.json') as json_file:
    data4 = json.load(json_file)
    data.update(data4)

#Clean json file
temp_data = {}
for key,game in data.items():
    if "Genre" in game:
        game['Genres'] = game.pop('Genre')
    if "Platform" in game:
        game['Publishers'] = game.pop('Publisher')
    if "Developer" in game:
        game['Developers'] = game.pop('Developer')
    temp_data[key] = game
data = temp_data
del(temp_data)
data_file = open('data_file.csv', 'w')

#Create the csv writer object
csv_writer = csv.writer(data_file)

#Write header data first
#The first minimun value is 22501 but, it can be change to 0 because
#all games will have the same headers
header = data["22654"].keys()
csv_writer.writerow(header)

for game_id in data:
    try:
        #Writing data of CSV file
        csv_writer.writerow(data[game_id].values())
    except Exception as e:
        pass

data_file.close()
