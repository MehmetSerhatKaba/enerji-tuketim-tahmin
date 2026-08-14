import requests
import pandas as pd

# Sceaux, Fransa koordinatları (smart meter verisinin toplandığı yer)
LATITUDE = 48.78
LONGITUDE = 2.29

# Veri setiyle aynı tarih aralığı
START_DATE = "2006-12-16"
END_DATE = "2010-11-26"

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation",
    "timezone": "Europe/Paris"
}

print("Hava durumu verisi çekiliyor...")
response = requests.get(url, params=params)

# İstek başarılı mı kontrol et
if response.status_code == 200:
    data = response.json()
    
    # 'hourly' kısmını DataFrame'e çevir
    weather_df = pd.DataFrame(data["hourly"])
    
    print("Çekme tamamlandı. Veri boyutu:", weather_df.shape)
    print(weather_df.head())
    
    weather_df.to_csv("ham_veri/hava_durumu_data.csv", index=False)
    print("Kaydedildi: ham_veri/hava_durumu_data.csv")
else:
    print("Hata oluştu! Status code:", response.status_code)
    print(response.text)