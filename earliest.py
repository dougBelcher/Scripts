# earliest - takes two strings representing dates and returns the string that represents the earliest point in time
import datetime


# def get_earliest1(first, second):
#     first_date = datetime.datetime.strptime(first, '%m/%d/%Y')
#     second_date = datetime.datetime.strptime(second, '%m/%d/%Y')
#     if second_date < first_date:
#         return second
#     else:
#         return first


def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    m1, d1, y1 = date1.split('/')
    m2, d2, y2 = date2.split('/')
    if (y1, m1, d1) < (y2, m2, d2):
        return date1
    else:
        return date2


# def get_earliest(*dates):
#     """Return earliest of given MM/DD/YYYY-formatted date strings."""
#     def date_key(date):
#         (m, d, y) = date.split('/')
#         return (y, m, d)
#     return min(dates, key=date_key)


# print(f'earliest 1: {get_earliest("01/17/1832", "01/27/1756")}')    # year & day dif; mth diff
# print(f'earliest 2: {get_earliest("02/29/1972", "12/21/1946")}')    # year, mth, day diff
# print(f'earliest 3: {get_earliest("02/24/1946", "03/21/1946")}')    # year same; mth & day diff
# print(f'earliest 4: {get_earliest("06/24/1958", "06/21/1958")}')    # year & mth same; day diff
# print(f'earliest 5: {get_earliest("02/29/2006", "02/28/2006")}')    # year & mth same; day diff; inv day
# print(f'earliest 6: {get_earliest("02/30/2006", "02/29/2006")}')    # year & mth same; day diff; inv day
