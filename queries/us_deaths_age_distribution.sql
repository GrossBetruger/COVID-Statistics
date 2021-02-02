select age_group_new age_group,
       round(cast(covid_19_deaths as float) / total_deaths, 4) * 100 as 'percent of all deaths',
       cast(covid_19_deaths as intger),
       cast(total_deaths as integer)
from us_corona_deaths_age_and_sex
where state = 'United States'
and sex = 'All Sexes'
;

