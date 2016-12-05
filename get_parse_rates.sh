cd /home/admin/exchange-rates/exchange-rates-usd
wget https://fred.stlouisfed.org/categories/94/downloaddata/INTLFXD_csv_2.zip -O data/INTLFXD_csv_2.zip
python run.py
git commit data/consolidated.csv -m "Update consolidated CSV"
git push

