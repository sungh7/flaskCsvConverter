import csv, json
csv_file_path = 'csv_DB/290925814.jpg.csv'
json_file_path = 'json_DB/20925814.jpg.csv'

data = {}
with open(csv_file_path) as csvFile:
    csv_reader = csv.DictReader(csvFile)
    for rows in csv_reader:
        id = rows['id']
        data[id] = rows

with open(json_file_path, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))