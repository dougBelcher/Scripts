# days until the 2020 election
import datetime
from datetime import date


def election():
    election_date = datetime.date(2021, 1, 20)
    today = date.today()
    print(f'Inauguration date ({election_date}) - today ({today}) = days to go: {election_date - today}')


if __name__ == "__main__":
    election()
