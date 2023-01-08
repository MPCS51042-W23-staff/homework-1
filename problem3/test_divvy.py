from towing import top_days, day_summary


def test_day_summary_length():
    assert len(day_summary()) == 30


def test_day_summary_ordering():
    summary = day_summary()
    assert summary[0][0] == "06/26/2022"
    assert summary[1][0] == "06/18/2022"
    assert summary[20][0] == "06/01/2022"
    assert summary[-2][0] == "06/08/2022"
    assert summary[-1][0] == "06/06/2022"


def test_say_summary_values():
    summary = day_summary()
    assert summary[0][1] == 227
    assert summary[1][1] == 218
    assert summary[20][1] == 155
    assert summary[-2][1] == 100
    assert summary[-1][1] == 84


def test_top_n3():
    assert top_days(3) == [
        ('06/26/2022', 227),
        ('06/18/2022', 218), 
        ('06/11/2022', 207)
    ]


def test_top_n10():
    assert top_days(10) == [
        ('06/26/2022', 227),
        ('06/18/2022', 218),
        ('06/11/2022', 207),
        ('06/17/2022', 198),
        ('06/23/2022', 193),
        ('06/24/2022', 191),
        ('06/20/2022', 191),
        ('06/03/2022', 190),
        ('06/05/2022', 189),
        ('06/19/2022', 184),
    ] or top_days(10) == [
        ('06/26/2022', 227),
        ('06/18/2022', 218),
        ('06/11/2022', 207),
        ('06/17/2022', 198),
        ('06/23/2022', 193),
        ('06/20/2022', 191),
        ('06/24/2022', 191),
        ('06/03/2022', 190),
        ('06/05/2022', 189),
        ('06/19/2022', 184),
    ]
