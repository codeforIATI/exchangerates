Code for producing consolidated historical exchange rate data from the St Louis Federal Reserve.

See also <http://thedatahub.org/dataset/exchange-rates>

Instructions
============

Run the script:

    ./get_parse_rates.sh

This will get the source data dumps into the data/ directory and run the Python script to generate consolidated data. This bash script is designed to be run as a cron job.

Or if you have the data already downloaded then run:

    python run.py

Result will be at data/consolidated.csv.

