# ⚡ Enerji Tüketim Veri Ambarı ve Tahmin Platformu

Akıllı sayaç tüketim verisini hava durumu verisiyle birleştiren; temizleyen,
boyutsal olarak modelleyen ve üzerine bir zaman serisi tahmin modeli kuran
uçtan uca bir veri mühendisliği projesi.

> Veri mühendisliğinde işe alım sürecinde en çok aranan beceriler tek bir
> akışta birleşiyor: veri alımı, veri kalitesi kontrolü, boyutsal modelleme
> (star schema) ve makine öğrenmesi entegrasyonu.

---

## 📐 Mimari

Pipeline, her biri bağımsız olarak çalıştırılabilen ve test edilebilen
katmanlardan oluşur:

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│    ALIM      │──▶│  DEPOLAMA    │──▶│  DÖNÜŞÜM     │──▶│  MAKİNE ÖĞ.  │
│ Python        │   │  DuckDB      │   │  dbt         │   │  Prophet     │
│ REST API/CSV │   │  Yerel DWH   │   │  Star schema │   │  + MLflow    │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

**Veri akışı:**

1. **Alım** — Enerji tüketim verisi ve Open-Meteo API üzerinden hava durumu
   verisi Python betikleriyle çekilir.
2. **Depolama** — Ham veri yerel bir DuckDB veri ambarına yüklenir.
3. **Dönüşüm** — dbt ile ham veri, staging katmanından geçirilip
   dimension/fact tablolarına dönüştürülerek **star schema** kurulur.
4. **Makine öğrenmesi** — Prophet ile saatlik tüketim üzerinde zaman serisi
   tahmini yapılır; her deney MLflow ile kayıt altına alınır.

## 🗂️ Star Schema Veri Modeli

| Katman | Model | Açıklama |
|---|---|---|
| Staging | `stg_enerji` | Temizlenmiş ve dönüştürülmüş ham enerji verisi |
| Dimension | `dim_zaman` | Zaman boyutu (tarih/saat kırılımları) |
| Dimension | `dim_lokasyon` | Lokasyon boyutu |
| Fact | `fact_tuketim` | Aktif güç tüketimi olgu tablosu |

Her model için dbt üzerinde `not_null` ve `unique` testleri tanımlıdır
(`dbt_proje/models/schema.yml`).

## 📁 Proje Yapısı

```
enerji-tuketim-tahmin/
├── indir_veri.py                  # Enerji tüketim verisini indirir
├── hava_durumu_indir.py           # Open-Meteo API'den hava durumu verisi çeker
├── kesfedici_analiz.ipynb         # Keşifçi veri analizi (EDA)
├── ozellik_muhendisligi.ipynb     # Özellik mühendisliği
├── veri_kalite_testleri.ipynb     # Veri kalitesi kontrolleri
├── model_egitimi.ipynb            # Tahmin modeli eğitimi
├── prophet_mlflow.ipynb           # Prophet + MLflow deney takibi
└── dbt_proje/
    ├── models/
    │   ├── staging/stg_enerji.sql
    │   ├── dimension/dim_zaman.sql
    │   ├── dimension/dim_lokasyon.sql
    │   └── fact/fact_tuketim.sql
    ├── tests/
    └── dbt_project.yml
```

## 🛠️ Teknoloji Yığını

| Katman | Araç |
|---|---|
| Dil | Python (Pandas) |
| Veri alımı | REST API (Open-Meteo), CSV |
| Veri ambarı | DuckDB |
| Dönüşüm / modelleme | dbt |
| Veri kalitesi | Great Expectations |
| Makine öğrenmesi | Prophet (zaman serisi tahmini) |
| Deney takibi | MLflow |
| Ortam | Jupyter Notebook |

## 🚀 Kurulum

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install pandas prophet mlflow dbt-core dbt-duckdb duckdb great_expectations jupyter
```

> **Not:** Proje sanal ortamı (`venv/`) ile ham/temiz veri klasörleri
> (`ham_veri/`, `temiz_veri/`) ve eğitilmiş model çıktıları (`model/`,
> `mlruns/`) boyut nedeniyle bu depoya dahil değildir; `.gitignore` ile hariç
> tutulmuştur. Veri, `indir_veri.py` ve `hava_durumu_indir.py`
> betikleriyle yeniden üretilebilir.

## ▶️ Çalıştırma Sırası

1. **Veri toplama**
   ```bash
   python indir_veri.py
   python hava_durumu_indir.py
   ```
2. **Keşifçi analiz ve özellik mühendisliği** — `kesfedici_analiz.ipynb` ve
   `ozellik_muhendisligi.ipynb` notebook'larını sırayla çalıştır.
3. **Veri kalite testleri** — `veri_kalite_testleri.ipynb`
4. **dbt ile boyutsal modelleme**
   ```bash
   cd dbt_proje
   dbt run
   dbt test
   ```
5. **Tahmin modeli ve deney takibi** — `model_egitimi.ipynb` ve
   `prophet_mlflow.ipynb` notebook'larını çalıştır; deneyler MLflow
   arayüzünden (`mlflow ui`) izlenebilir.

## ✅ Kapsanan Konular

- [x] REST API ve CSV ile veri alımı
- [x] Star schema / boyutsal veri ambarı tasarımı
- [x] dbt ile test edilmiş ve dokümante edilmiş modeller
- [x] Veri kalitesi doğrulama
- [x] Prophet ile zaman serisi tahmini
- [x] MLflow ile deney takibi ve model versiyonlama

## 🔭 Sıradaki Adımlar

- Airflow ile günlük otomatik çalışan bir orkestrasyon katmanı eklemek
- Metabase üzerinde bölge bazlı tüketim ve tahmin/gerçek karşılaştırma
  dashboard'u kurmak
- Streaming ve modern lakehouse mimarisine (Kafka, Flink, Delta Lake)
  taşımak
