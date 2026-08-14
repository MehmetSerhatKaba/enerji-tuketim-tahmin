# Enerji Tüketim Tahmin Platformu

Elektrik tüketim verisini hava durumu verisiyle birleştirip zaman serisi
modeliyle tüketim tahmini üreten uçtan uca bir veri mühendisliği projesi.

## Genel Akış

1. **Veri toplama** — `indir_veri.py` ve `hava_durumu_indir.py` ile ham
   enerji tüketim ve hava durumu verileri indirilir.
2. **Veri modelleme (dbt)** — `dbt_proje/` altında ham veri, boyut (dimension)
   ve olgu (fact) tablolarına dönüştürülerek yıldız şema (star schema)
   kurulur:
   - `models/staging/stg_enerji.sql`
   - `models/dimension/dim_zaman.sql`, `dim_lokasyon.sql`
   - `models/fact/fact_tuketim.sql`
3. **Keşifçi veri analizi** — `kesfedici_analiz.ipynb`
4. **Özellik mühendisliği** — `ozellik_muhendisligi.ipynb`
5. **Veri kalite testleri** — `veri_kalite_testleri.ipynb`
6. **Model eğitimi** — `model_egitimi.ipynb`, `prophet_mlflow.ipynb`
   Prophet ile zaman serisi tahmini, MLflow ile deney takibi ve model
   versiyonlama.

## Teknolojiler

Python (Pandas), Prophet, MLflow, dbt, DuckDB, Jupyter

## Kurulum

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt   # bkz. not aşağıda
```

> **Not:** `requirements.txt` bu depoya dahil değil; proje sanal ortamı
> (`venv/`) `.gitignore` ile hariç tutulmuştur. Kullanılan başlıca kütüphaneler:
> `pandas`, `prophet`, `mlflow`, `dbt-core`, `dbt-duckdb`, `duckdb`,
> `great_expectations`, `jupyter`.

Ham/temiz veri klasörleri (`ham_veri/`, `temiz_veri/`) ve eğitilmiş model
çıktıları (`model/`, `mlruns/`) boyut nedeniyle bu depoya dahil değildir;
`indir_veri.py` ve `hava_durumu_indir.py` betikleriyle yeniden üretilebilir.

## dbt Çalıştırma

```bash
cd dbt_proje
dbt run
dbt test
```
