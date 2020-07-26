# COVID Statistics USA (CDC data)

## This repo contains data from the CDC and scripts to update said data and dump it to an sqlite db. Example queries are also provided 


### how to use: 

```bash 
./download_raw_data.py # will download raw CSVs from CDC
```

```bash
./update_db.sh # will merge all CSV data into an sqlite db (path: corona_us_deaths.db) and send you to the sqlite interactive shell
```

### example queries can be found under:
```bash
queries/
```
