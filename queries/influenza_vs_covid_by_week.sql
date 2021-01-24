select cast(influenza_deaths as integer) "Influenza Deaths",
       cast(covid_19_deaths as integer) "COVID-19 Deaths",
       datetime(end_date) "week (end date)"
from corona_us_deaths
where state = 'United States'
order by "week (end date)"
;

