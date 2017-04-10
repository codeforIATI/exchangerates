A module to make it easier to handle historical exchange rates.

Currently combines daily rates from the St Louis Federal Reserve with monthly rates from the OECD.

See also <http://thedatahub.org/dataset/exchange-rates>

Instructions
============

Create a CurrencyConverter object:

    import exchangerates
    converter = exchangerates.CurrencyConverter(update=True)
    
Note: `update=True` will lead to fresh exchange rates being downloaded.

Get a list of the available currencies:

    print converter.known_currencies()
    
Get the conversion rate for a specific currency and date:
    
    print converter.closest_rate("USD", datetime.date(2012,7,20))
    print converter.closest_rate("EUR", datetime.date(2014,7,20))
    print converter.closest_rate("EUR", datetime.date(2014,7,20))

You can also just generate a consolidated file of exchange rates:

    python get_rates.py

Result will be at `data/consolidated_rates_.csv`.

