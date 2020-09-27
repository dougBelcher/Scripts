# days until the 2020 election
import datetime
from datetime import date


def election():
    election_date = datetime.date(2020, 11, 3)
    today = date.today()
    print(f'today ({today}) - election date ({election_date}) = days to go: {election_date - today}')


if __name__ == "__main__":
    election()
