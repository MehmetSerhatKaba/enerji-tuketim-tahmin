from ucimlrepo import fetch_ucirepo
import pandas as pd

# UCI'den veri setini çek (id=235, Individual Household Electric Power Consumption)
print("Veri indiriliyor, bu biraz zaman alabilir (2 milyon satır)...")
dataset = fetch_ucirepo(id=235)

# Özellikler (X) ve hedef (y) ayrı geliyor, birleştirelim
X = dataset.data.features
y = dataset.data.targets

# Tüm veriyi tek bir tabloda topla
df = pd.concat([X, y], axis=1)

print("İndirme tamamlandı. Veri boyutu:", df.shape)
print(df.head())

# Yerel diske CSV olarak kaydet
df.to_csv("ham_veri/smart_meter_data.csv", index=False)
print("Kaydedildi: ham_veri/smart_meter_data.csv")