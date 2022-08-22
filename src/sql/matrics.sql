insert into WEATHER_DATA_MATRICS
select region, strftime('%Y',record_date) as "Year",  avg(min_temp), avg(max_temp), sum(amount)
from WEATHER_DATA
where min_temp != -9999 and max_temp != -999 and amount != 9999
group by region, strftime('%Y',record_date)
;
