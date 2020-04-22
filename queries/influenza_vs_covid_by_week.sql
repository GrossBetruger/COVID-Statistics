select datetime(substr("Start week", 7, 4) || '-' || substr("Start week", 1, 2) || '-' || substr("Start week", 4, 2)) as 'Week',
       cast(replace("All COVID-19 Deaths (U07.1)", ',', '') as integer) as 'COVID Deaths',
       cast(replace("All Influenza Deaths (J09-J11)", ',', '') as integer) as 'Influenza Deaths'
from corona_us_deaths
where "Group" = 'By week'
and Indicator != 'Total Deaths'
;
