import pymysql
import requests
import json
import sys

def translate(en_word):
    res = requests.post('http://fanyi.youdao.com/translate?&doctype=json&type=', data=data1)
    content= json.loads(res.text)
    trans = content['translateResult'][0][0]['tgt']
    return trans

f1 = open(sys.argv[3],'r')
Field = f1.readlines()
list1 = []
list2 = []
list3 = []
for i in Field:
    a = i.split('/')
    for j in a:
        list1.append(j)
for i in list1:
    a = i.split(':')
    for j in a:
        list2.append(j)
for i in list2:
    a = i.split( )
    for j in a:
        list3.append(j)
b = len(list3)/3
db = pymysql.connect(
host = '127.0.0.1',
user = sys.argv[1],
password = sys.argv[2],
database = 'foodmart',
port = 3306,
charset = 'utf8'
)
cursor = db.cursor()
a = 1
result = []
result1 = []
for i in range(int(b)):
    cursor.execute('select '+list3[a]+' from '+list3[0]+'')
    result = cursor.fetchall()
    a = a+3
    result1.append(result)
list=[]
for data in result1:
    for r_data in data:
        if not r_data in list:
          list.append(r_data)
print(list)
for i in list:
    for j in i:
        while str(j).encode('UTF-8').isalpha() ==  False:
            en_word = str(j)
            data1 = {}
            data1['i'] = en_word
            data1['from'] = 'AUTO'
            data1['to'] = 'AUTO'
            ch_word = translate(en_word)
            txt = en_word + '=' + ch_word
            f = open(sys.argv[4], 'a+')
            f.write(txt + '\n')
            f.close()
            break
print('close')
cursor.close()
db.close()




