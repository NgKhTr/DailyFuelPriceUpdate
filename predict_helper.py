import pandas as pd
import constants
import state_helper
import gc

from statsmodels.tsa.arima.model import ARIMA

def predict(data: dict, current_date: pd.Timestamp):
    # Chuyển dữ liệu thành dataframe
    if current_date > pd.Timestamp(data[-1]["Date"]):
        data.append({"Date": current_date.strftime(constants.DATE_FORMAT)})

    df = pd.DataFrame(data)

    df['Date'] = pd.to_datetime(df['Date'], format=constants.DATE_FORMAT)
    df.set_index("Date", inplace=True)
    # print(df)
    # print(df.index[df.index.duplicated()])
    df = df.resample(pd.Timedelta(days=1)).ffill().ffill() # ffill cuối là để fill vào cái nan được bỏ qua ở cuối khi append

    print(df.shape)
    preds = {}
    for label in df:
        sr = df[label]
        model = ARIMA(sr, order=(constants.P, constants.D, constants.Q))
        model_fit = model.fit()

        preds[label] = model_fit.forecast(steps=constants.PREDICT_LENGTH)

        del model_fit
        gc.collect()

    df_pred = pd.DataFrame(preds)
    df_pred.index.name = "Date"
    df_pred.reset_index(drop=False, inplace=True)
    df_pred["Date"] = df_pred["Date"].dt.strftime(constants.DATE_FORMAT)
    return df_pred.to_dict("records")
if __name__ == "__main__":
    data = [
        {
            "Date": "2024-06-23",
            "Xăng RON 95-III": 22.27,
            "Xăng E5 RON 92-II": 23.21,
        },
        {
            "Date": "2024-06-30",
            "Xăng RON 95-III": 21.75,
            "Xăng E5 RON 92-II": 19.9
        }]
    print(predict(data, pd.Timestamp("2024-07-03")))
    pass