select start_week,
       round(cast(replace(covid_deaths, ',', '') as integer) * 1.0 /
       cast(replace(total_deaths, ',', '') as integer) * 100, 2) as 'Percent of Deaths',
       covid_deaths,
       total_deaths
from corona_us_deaths
where "Group" = 'By week'
and state = 'United States'
;

