import constants
import requests
import json


def get(from_date=None):
    response = requests.get(constants.DATABASE_URL, params={"fromDate": from_date})
    # test
    # print(response)
    # end test

    data = response.json()
    return data

def post(
    Predict,
    Data=None,
):
    data = {"Data": Data, "Predict": Predict}
    response = requests.post(constants.DATABASE_URL, data=json.dumps(data))
    return response


if __name__ == "__main__":
    # print(get())
    #  contents = {
    Data = [
        {
            "Date": "2024-06-23",
            "Xăng RON 95-III": 22.27,
            "Xăng E5 RON 92-II": 23.21,
        },
        {
            "Date": "2024-06-30",
            "Xăng RON 95-III": 21.75,
            "Xăng E5 RON 92-II": 22.51,
        },
        {
            "Date": "2024-07-06",
            "Xăng RON 95-III": 21.14,
            "Xăng E5 RON 92-II": 21.97,
        },
        {
            "Date": "2024-07-13",
            "Xăng RON 95-III": 21.31,
            "Xăng E5 RON 92-II": 22.23,
        },
        {"Date": "2024-07-20", "Xăng RON 95-III": 21.5, "Xăng E5 RON 92-II": 22.46},
    ]
    Predict = [
        {"Date": "2024-08-21", "Xăng RON 95-III": 22.27, "Xăng E5 RON 92-II": 23.21},
        {"Date": "2024-08-22", "Xăng RON 95-III": 21.75, "Xăng E5 RON 92-II": 22.51},
        {"Date": "2024-08-23", "Xăng RON 95-III": 21.14, "Xăng E5 RON 92-II": 21.97},
        {"Date": "2024-08-24", "Xăng RON 95-III": 21.31, "Xăng E5 RON 92-II": 22.23},
        {"Date": "2024-08-25", "Xăng RON 95-III": 21.5, "Xăng E5 RON 92-II": 22.46},
    ]

    import pandas as pd
    import pytz
    import time

    timezone = pytz.timezone('Asia/Ho_Chi_Minh')
    current = pd.Timestamp.now(tz=timezone).tz_localize(None)
    
    from_date = current - pd.Timedelta(days=constants.DAYS_GAP_FOR_TRAIN)
    old_data = get(from_date.strftime(constants.DATE_FORMAT))
    print(from_date.strftime(constants.DATE_FORMAT))
    print(old_data[0])
    pass