import pandas as pd


def top_days(n):
    """
    Returns the top days that divvy bike rides were started.

    Inputs:
        n (int): Number of days to return.

    Output:
        A list of tuples where the first item is a start_date and the second item the number of bike rides started on that date.
        There should only be 'n' elements, ordered by bike rides that were started on the day.

        For example:
            [
              ('06/26/2022', 227),
              ('06/18/2022', 218),
              ('06/11/2022', 207),
            ]
    """
    data = load_data()
    counter = dict()
    for i in data.index:
        start_date = data['start_date'][i]
        if start_date in counter:
            counter[start_date] += 1
        else:
            counter[start_date] = 1

    top_n_dates = list(dict(sorted(counter.items(), key=lambda item: item[1], reverse=True)).keys())[:n]

    list_tuples = list()
    for d in top_n_dates:
        list_tuples.append((d, counter[d]))

    return list_tuples


def day_summary():
    """
    Return a list of all days in chronological order, along with the number of bike rides started for that date

    Output:
        A list of tuples where the first item is a date and the second item is the number of bike rides started for that date.

        For example:
            [
              ('06/26/2022', 227),
              ('06/18/2022', 218),
              ('06/11/2022', 207),
              ... # truncated
              ('06/30/2022', 149),
            ]
    """
    data = load_data()
    counter = dict()
    for i in data.index:
        start_date = data['start_date'][i]
        if start_date in counter:
            counter[start_date] += 1
        else:
            counter[start_date] = 1

    top_n_dates = list(dict(sorted(counter.items(), key=lambda item: item[1], reverse=True)).keys())

    list_tuples = list()
    for d in top_n_dates:
        list_tuples.append((d, counter[d]))

    return list_tuples


def load_data():
    df = pd.read_csv('problem3/divvy.csv')
    return df
