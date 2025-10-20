import requests
#datetime物件
from datetime import datetime
import sys
import matplotlib.pyplot as plt

#列出此城市五日平均溫度
address = input("請輸入城市名稱（例如 Taipei）：")

url = f"https://api.openweathermap.org/data/2.5/forecast?q={address}&appid=6feeb2fd1fa510b1572702ab8680c2a5&units=metric&lang=zh_tw"
response = requests.get(url)
data = response.json()

if data['cod'] != '200':
     print("找不到這個城市，請確認名稱是否正確。")
     sys.exit()

tempDict = {}

for item in data['list']:
    temp = item['main']['temp']
    date = item['dt_txt']
    #轉datetime物件: 1.取日期跟時間 2.時間比較
    dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    dtDate = dt.date()
    if dtDate in tempDict:
        tempDict[dtDate].append(temp)
    else:
        tempDict[dtDate] = [temp]

#快速建立dict
avgTempDict = {d: sum(t) / len(t) for d, t in tempDict.items()}

plt.plot(avgTempDict.keys(), avgTempDict.values(), marker='o')
plt.title("Daily average Temperature variation")
plt.xlabel("日期")
plt.xticks(rotation=45)
plt.ylabel("溫度")
plt.show()