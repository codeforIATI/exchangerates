import csv
import zipfile
import datetime
from lxml import etree

fp = 'data/OECD_rates.xml'
outfp = 'data/consolidated.csv'

def make_date(value):
  return datetime.datetime.strptime(value, "%Y-%m-%d")

countries_currencies = {
  'AUS': 'AUD',
  'BRA': 'BRL',
  'CAN': 'CAD',
  'CHE': 'CHF',
  'CHL': 'Chile',
  'CHN': "CNY",
  'COL': 'Colombia',
  'CRI': 'Costa Rica',
  'CZE': 'CZK',
  'DNK': 'DKK',
  'EA19': 'EUR',
  'GBR': 'GBP',
  'HUN': 'HUF',
  'IDN': 'Indonesia',
  'IND': 'INR',
  'ISL': 'Iceland',
  'ISR': 'Israel',
  'JPN': 'JPY',
  'KOR': 'Korea',
  'LVA': 'Latvia',
  'MEX': 'MXN',
  'NOR': 'NOK',
  'NZL': 'NZD',
  'POL': 'Poland',
  'RUS': 'Russia',
  'SDR': 'SDR',
  'SWE': 'SEK',
  'TUR': 'Turkey',
  'ZAF': 'ZAR'
  }

# Find earliest data for each currency from the St Louis Fed data
def get_earliest_dates():
  outfp_file = open(outfp, "r")
  reader = csv.DictReader(outfp_file)
  indata = list(map(lambda row: row, reader))
  outfp_file.close()
  
  currencies = dict(map(lambda currency: 
                          (currency, None), 
              list(set(map(lambda row: row["Currency"], indata)))))

  for currency in currencies:
    currency_dates = list(map(lambda y: 
              make_date(y["Date"]),
            filter(lambda x: x['Currency'] == currency, indata)
    ))
    currencies[currency] = min(currency_dates)
  
  return currencies

def get_OECD_data(writer, currencies_dates):
  fp_doc = etree.parse(fp)
  nsmap = {
    "ns":"http://www.SDMX.org/resources/SDMXML/schemas/v2_0/generic"
  }
  
  print "Earliest dates are {}".format(currencies_dates)
  
  series = fp_doc.findall("ns:DataSet/ns:Series", namespaces=nsmap)
  for serie in series:
    currency = serie.find("ns:SeriesKey/ns:Value[@concept='LOCATION']", namespaces=nsmap).get("value")
    
    min_currency_date = currencies_dates.get(
          countries_currencies.get(currency), 
          datetime.datetime.utcnow())
    
    for obs in serie.findall("ns:Obs", namespaces=nsmap):
      date = "{}-01".format(obs.find("ns:Time", namespaces=nsmap).text)
      value = obs.find("ns:ObsValue", namespaces=nsmap).get("value")
      if make_date(date) < min_currency_date:
        writer.writerow([date, value, countries_currencies.get(currency), "M", "OECD"])

def run():
    currencies_dates = get_earliest_dates()
    writer = csv.writer(open(outfp, 'ab'))
    get_OECD_data(writer, currencies_dates)

run()

