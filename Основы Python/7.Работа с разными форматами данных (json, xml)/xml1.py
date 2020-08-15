import xml.etree.cElementTree as cET
from collections import Counter

tree = cET.ElementTree(file='file.xml')
root = tree.getroot()
str1 = ''
output = []

message = root.findall('channel/item/description')
for i in message:
    str1 += i.text
message = root.findall('channel/item/title')
for i in message:
    str1 += i.text

str2 = str1.split()

str2.sort()

for i in str2:
    if len(i) >= 6:
        output.append(i)

print(Counter(output).most_common(10))