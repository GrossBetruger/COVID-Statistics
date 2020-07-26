with agg_new_york as (
    select
    case when  state like  'New York%' then 'New York' else state end as state,
    covid_deaths
    from corona_us_deaths
)
select sum(covid_deaths) covid_deaths_in_state, state
from agg_new_york
where state != 'United States'
group by state
order by covid_deaths_in_state desc
;

