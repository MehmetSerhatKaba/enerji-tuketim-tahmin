with stg as (
    select * from {{ ref('stg_enerji') }}
),

zaman as (
    select * from {{ ref('dim_zaman') }}
)

select
    stg.datetime,
    stg.aktif_guc,
    stg.reaktif_guc,
    stg.voltaj,
    stg.akim,
    stg.sayac_1,
    stg.sayac_2,
    stg.sayac_3,
    stg.sicaklik,
    stg.nem,
    stg.yagis,
    zaman.saat,
    zaman.haftanin_gunu,
    zaman.ay,
    zaman.yil,
    zaman.hafta_sonu,
    zaman.mevsim,
    1 as lokasyon_id
from stg
left join zaman using (datetime)