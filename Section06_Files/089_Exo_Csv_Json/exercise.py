# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json

fp = open('csv_file.txt', 'r')
lines = fp.readlines()
fp.close()

# print(lines)
lines = [c.strip() for c in lines]
# print(lines)

lines_to_json = []
for line in lines:
    print(line)
    club = line.split(',')[0]
    city = line.split(',')[1]
    country = line.split(',')[2]
    dic = {'club': club, 'city': city, 'country': country}
    lines_to_json.append(dic)

print(lines_to_json)
fp1 = open('json_file.txt', 'w')
json.dump(lines_to_json, fp1, indent=6)
fp1.close()
