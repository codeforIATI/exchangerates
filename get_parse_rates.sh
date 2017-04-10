#!/bin/bash
wget https://fred.stlouisfed.org/categories/94/downloaddata/INTLFXD_csv_2.zip -O data/INTLFXD_csv_2.zip
python run.py
wget "http://stats.oecd.org/restsdmx/sdmx.ashx/GetData/MEI_FIN/CCUS.AUS+AUT+BEL+CAN+CHL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+EA19+SDR+NMEC+BRA+CHN+COL+CRI+IND+IDN+RUS+ZAF.M/all?startTime=1950-01" -O data/OECD_rates.xml
./pyenv/bin/python run_oecd.py
git commit data/consolidated.csv -m "Update consolidated CSV"
git push

