import csv,json

with open('data.csv', 'r') as file_csv:
    fieldnames = ("color1","bg1","color2","bg2","correct_response")
    reader = csv.DictReader(file_csv, fieldnames)

    with open('data.json', 'w') as file_json:
        file_json.write('{"data":[')
        for row in reader:
                json.dump(row, file_json)
                file_json.write(',')
        file_json.write(']}')
