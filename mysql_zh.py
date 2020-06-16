import pymysql
import re
import sys

def lj_field(field,list):
    for i in field:
        for j in i:
            if j == list[2]:
                return 1
    return 0

def lj_mysql(leng,list1,cursor):
    a = 1
    result1 = []
    for i in range(int(leng)):
        cursor.execute('select ' + list1[a] + ' from '+list1[0]+'')
        result = cursor.fetchall()
        a = a + 3
        result1.append(result)
    return result1
def find_word(list,word,line):
    for i in range(0,line):
        a = list[i].find(word)
        if a != -1:
            return i

def find_zh(data,num):
    str = re.sub("[A-Za-z0-9\!\%\[\]\,\。\=\' '\\n\.\-]", "", data[num])
    return str

def translate_mysql(en,ch):
    for i in result:
        for j in i:
            for k in j:
                en.append(k)
                print(en)
                num = find_word(data, str(k), line)
                zh = find_zh(data, num)
                ch.append(zh)

db = pymysql.connect(
    host='127.0.0.1',
    user=sys.argv[1],
    password=sys.argv[2],
    database='foodmart',
    port=3306,
    charset='utf8'
)
cursor = db.cursor()
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
cursor.execute('select * from '+list3[0]+'')
field = cursor.fetchall()
a = lj_field(field,list3)
leng = len(list3)/3
if a == 0:
    j = 2
    for i in range(int(leng)):
        cursor.execute('alter table '+list3[0]+' add ' + list3[j] + ' varchar(30)')
        cursor.connection.commit()
        j = j+3
result = lj_mysql(leng,list3,cursor)
f3 = open(sys.argv[4],'r')
data = f3.readlines()
line= len(data)
a = 1
b = 0
ch = []
en = []
translate_mysql(en,ch)
line1 = len(ch)/leng
for i in range(0,int(leng)):
    for j in range(0,int(line1)):
        print(list3[a+1],ch[b],list3[a],en[b])
        cursor.execute("update "+list3[0]+" set "+list3[a+1]+"= '" + ch[b] + "' where "+list3[a]+" = '" + en[b] + "'")
        cursor.connection.commit()
        b = b+1
    a = a+3