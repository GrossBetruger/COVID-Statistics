select cast(strftime('%s', datetime(substr("Start week", 7, 4) || '-' || substr("Start week", 1, 2) || '-' || substr("Start week", 4, 2))) as int) as 'timestamp',
       datetime(substr("Start week", 7, 4) || '-' || substr("Start week", 1, 2) || '-' || substr("Start week", 4, 2)) as 'Week',
       round(cast(replace("All COVID-19 Deaths (U07.1)", ',', '') as integer) * 1.0 /
       cast(replace("Deaths from All Causes", ',', '') as integer) * 100, 2) as 'Percent of Deaths'
from corona_us_deaths
where "Group" = 'By week'
and Indicator != 'Total Deaths'
;
