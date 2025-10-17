import requests
#列出此城市五日平均溫度
address = input("請輸入城市名稱（例如 Taipei）：")

url = f"https://api.openweathermap.org/data/2.5/forecast?q={address}&appid=6feeb2fd1fa510b1572702ab8680c2a5&units=metric&lang=zh_tw"
response = requests.get(url)
data = response.json()

if data['cod'] != '200'
    return print("找不到這個城市，請確認名稱是否正確。")

for item in data['list']:
    temp = item['main']['temp']
    date = item['dt_txt']
