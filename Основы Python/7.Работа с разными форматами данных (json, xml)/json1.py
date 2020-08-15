import json
from collections import Counter

output = []
str1 = ''

with open('file.json', 'r', encoding="UTF-8") as JF:
    data = json.load(JF)

for i in data['rss']['channel']['items']:
    str1 += (i['description'] + ' ')
    str1 += (i['title'] + ' ')

str2 = str1.split()

str2.sort()

for i in str2:
    if len(i) >= 6:
        output.append(i)

print(Counter(output).most_common(10))