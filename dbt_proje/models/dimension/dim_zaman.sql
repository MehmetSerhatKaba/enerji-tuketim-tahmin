with stg as (
    select distinct
        datetime,
        extract('hour' from datetime)       as saat,
        extract('dow' from datetime)        as haftanin_gunu,
        extract('month' from datetime)      as ay,
        extract('year' from datetime)       as yil,
        extract('doy' from datetime)        as yilin_gunu,
        case
            when extract('dow' from datetime) >= 5 then 1
            else 0
        end                                 as hafta_sonu,
        case
            when extract('month' from datetime) in (12,1,2) then 'Kış'
            when extract('month' from datetime) in (3,4,5)  then 'İlkbahar'
            when extract('month' from datetime) in (6,7,8)  then 'Yaz'
            else 'Sonbahar'
        end                                 as mevsim
    from {{ ref('stg_enerji') }}
)

select * from stg