# Read CSV file
import csv
from datetime import  datetime

result = {}
datas=[]
with open('trades.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')

    for val in reader:
        datas.append([datetime.strptime(val[0], '%H:%M:%S.%f'), val[3]])

    for i in range (0, len(datas)):
        k = datas[i][0]
        v = datas[i][1]
        value = 1
        for j in range(i+1, len(datas)):
            k1 = datas[j][0]
            v1 = datas[j][1]
            delta = k1 - k
            if delta.total_seconds() < 60:
                if v == v1:
                   value += 1
            else:
                break
        if v in result:
            if result[v] < value:
                result[v] = value

        else:
            result[v] = value
for k, v in sorted(result.items()):
    print(v)
