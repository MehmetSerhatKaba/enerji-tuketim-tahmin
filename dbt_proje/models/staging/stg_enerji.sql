with kaynak as (
    select * from read_csv_auto('../temiz_veri/birlesik_veri.csv')
),

donusturulmus as (
    select
        cast(datetime as timestamp)     as datetime,
        Global_active_power             as aktif_guc,
        Global_reactive_power           as reaktif_guc,
        Voltage                         as voltaj,
        Global_intensity                as akim,
        Sub_metering_1                  as sayac_1,
        Sub_metering_2                  as sayac_2,
        Sub_metering_3                  as sayac_3,
        temperature_2m                  as sicaklik,
        relative_humidity_2m            as nem,
        precipitation                   as yagis
    from kaynak
)

select * from donusturulmus