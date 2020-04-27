with pivot as (
    select (select "Non-Hispanic Black or African American"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Weighted distribution of population (%)'
           ) as weighted,
           (select "Non-Hispanic Black or African American"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Unweighted distribution of population (%)'
           ) as unweighted,
           (select "Non-Hispanic Black or African American"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Distribution of COVID deaths (%)'
           ) as 'Distribution of COVID deaths (%)',
           'black' as race

    union

        select (select "Non-Hispanic White"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Weighted distribution of population (%)'
           ) as weighted,
           (select "Non-Hispanic White"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Unweighted distribution of population (%)'
           ) as unweighted,
           (select "Non-Hispanic White"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Distribution of COVID deaths (%)'
           ) as 'Distribution of COVID deaths (%)',
           'white' as race

    union

        select (select "Hispanic or Latino"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Weighted distribution of population (%)'
           ) as weighted,
           (select "Hispanic or Latino"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Unweighted distribution of population (%)'
           ) as unweighted,
           (select "Hispanic or Latino"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Distribution of COVID deaths (%)'
           ) as 'Distribution of COVID deaths (%)',
           'hispanic' as race

      union

        select (select "Non-Hispanic Asian"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Weighted distribution of population (%)'
           ) as weighted,
           (select "Non-Hispanic Asian"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Unweighted distribution of population (%)'
           ) as unweighted,
           (select "Non-Hispanic Asian"
            from us_corona_deaths_race
            where State = 'United States'
              and Indicator = 'Distribution of COVID deaths (%)'
           ) as 'Distribution of COVID deaths (%)',
           'asian' as race
)
select round("Distribution of COVID deaths (%)" / unweighted, 2) as misrepresentation_rate,
       *
from pivot;

