select sum(covid_19_deaths) "COVID-19 Deaths", state "State"
from corona_us_deaths
where state != 'United States'
group by state
order by "COVID-19 Deaths" desc
;

