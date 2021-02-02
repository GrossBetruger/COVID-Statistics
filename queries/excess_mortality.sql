select date(start_date) "Week", cast(percent_of_expected_deaths as float)  "Percent of Expected Deaths"
from corona_us_deaths
where state = 'United States'
order by date(start_date) desc
;

