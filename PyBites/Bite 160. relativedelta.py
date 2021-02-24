# 160. More robust timedeltas (PyPI)
# Use relativedelta (python-dateutil) for more specific date calculations
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://pybit.es/python-dateutil.html

from datetime import date
from dateutil.relativedelta import relativedelta, MO

pybytes_born  = date(year=2016, month=12, day=19)
today = date.today()

diff = relativedelta(today, pybytes_born)
print(f'{diff.years} and {diff.months}')
