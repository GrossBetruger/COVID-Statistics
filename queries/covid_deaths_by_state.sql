with agg_new_york as (
    select cast(replace("All COVID-19 Deaths (U07.1)", ',', '') as integer) as 'COVID Deaths',
           case when
               Indicator in ('New York', 'New York City')
               then 'New York State'
               else Indicator end
               as Indicator
    from corona_us_deaths
    where "Group" = 'By state'
)
select Indicator State, sum("COVID Deaths") as COVID_Deaths from agg_new_york
where Indicator != 'Total US'
--where Indicator in ('California', 'New York State', 'New Jersey', 'Michigan', 'Massachusetts')
group by Indicator
order by COVID_Deaths desc
