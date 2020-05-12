select Indicator, "All COVID-19 Deaths (U07.1)", "Deaths from All Causes", "All Influenza Deaths (J09-J11)",
  round(cast(replace("All COVID-19 Deaths (U07.1)", ',', '') as float) / cast(replace("Deaths from All Causes", ',', '') as integer), 4) * 100 as "Percent of Deaths (COVID / All)" 
from corona_us_deaths
where "Group" = 'By age'
;
