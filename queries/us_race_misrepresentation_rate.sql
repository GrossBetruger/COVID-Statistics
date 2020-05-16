with blacks as (
    select non_hispanic_black_african_american as race, indicator
    from us_corona_deaths_race
    where state = 'United States'
),
whites as (
    select non_hispanic_white as race, indicator
    from us_corona_deaths_race
    where state = 'United States'
),
hispanic as (
    select hispanic_latino_total as race, indicator
    from us_corona_deaths_race
    where state = 'United States'
)
select 'blacks' as race, (select race from blacks where indicator = 'Distribution of COVID-19 deaths (%)')
               /
       (select race from blacks where indicator = 'Unweighted distribution of population (%)')
        as misrepresentation_rate
union

select 'whites' as race, (select race from whites where indicator = 'Distribution of COVID-19 deaths (%)')
               /
       (select race from whites where indicator = 'Unweighted distribution of population (%)')
        as misrepresentation_rate

union

select 'hispanic' as race, (select race from hispanic where indicator = 'Distribution of COVID-19 deaths (%)')
               /
       (select race from hispanic where indicator = 'Unweighted distribution of population (%)')
        as misrepresentation_rate
;

