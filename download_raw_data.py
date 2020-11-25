#!/bin/python

import requests

AGE_SEX_DATA_CSV = "us_covid_provisional_age_sex_data.csv"

RACE_DATA_CSV = "us_covid_provisional_race_data.csv"

WEEKLY_DATA_CSV = "us_covid_provisional_weekly_data.csv"

AGE_AND_SEX_DATA_URL = "https://data.cdc.gov/resource/9bhg-hcku.csv"

WEEKLY_DATA = "https://data.cdc.gov/resource/r8kw-7aab.csv"

RACE_DATA_URL = "https://data.cdc.gov/resource/pj7m-y5uh.csv"


if __name__ == "__main__":
    with open(WEEKLY_DATA_CSV, "wb") as f:
        f.write(requests.get(WEEKLY_DATA).content)

    with open(RACE_DATA_CSV, "wb") as f:
        f.write(requests.get(RACE_DATA_URL).content)

    with open(AGE_SEX_DATA_CSV, "wb") as f:
        f.write(requests.get(AGE_AND_SEX_DATA_URL).content)

    print("DONE")
