import pathlib
import pytest
import csv
from exchangerates import get_rates

def test_get_rates():
    filename = 'test_data_exchangerates.csv'
    get_rates.update_rates(filename)
    with open(filename, 'r') as infile:
        csvreader = csv.DictReader(infile)
        assert csvreader.fieldnames == [
            'Date', 'Rate', 'Currency',
            'Frequency', 'Source',
            'Country code', 'Country']
    pathlib.Path(filename).unlink()