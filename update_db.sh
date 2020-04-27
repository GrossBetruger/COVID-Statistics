#!/bin/bash

set -e

sqlite3 --cmd ".mode csv" --cmd ".import us_covid_provisional_weekly_data.csv corona_us_deaths" --cmd ".import us_covid_provisional_race_data.csv us_corona_deaths_race" --cmd ".save corona_us_deaths.db"

