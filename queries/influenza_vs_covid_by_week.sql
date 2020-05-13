select start_week as start_week,
       cast(replace(covid_deaths, ',', '') as integer) as 'COVID Deaths',
       cast(replace(influenza_deaths, ',', '') as integer) as 'Influenza Deaths'
from corona_us_deaths
where "group" = 'By week'
and state = 'United States'
order by start_week
;
