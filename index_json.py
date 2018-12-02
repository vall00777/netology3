import json
from collections import Counter
with open('newsafr.json', encoding='utf-8') as f:
    data = json.load(f)

out = []

for item in data["rss"]["channel"]["items"]:
     for i in item["description"].split():
         if len(i) > 6:
              out.append(i)

num = 1
for i, z in Counter(out).most_common(10):
     print('{0}. {1} - {2}'.format(num, i, z))
     num += 1

              
