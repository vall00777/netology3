from collections import Counter

import xml.etree.ElementTree as e
xmldoc = open('newsafr.xml', encoding='utf-8').read()
tree = e.fromstring(xmldoc)
b = tree.findall('channel')[0].iterfind('item')
out = []
for i in b:
     for i in i.find('description').text.split():
         if len(i) > 6:
              out.append(i)

num = 1
for i, z in Counter(out).most_common(10):
     print('{0}. {1} - {2}'.format(num, i, z))
     num += 1

              
