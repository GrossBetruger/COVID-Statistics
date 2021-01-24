select datetime(start_date) as start_week,
       cast(covid_19_deaths as integer) "COVID-19 Deaths",
       cast (influenza_deaths as integer) "Influenza Deaths"
from corona_us_deaths
where state = 'United States'
order by start_week
;

