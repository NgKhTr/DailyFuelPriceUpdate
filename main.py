import constants
import database_helper
import Notion_helper
import crawler_helper
import predict_helper
import pandas as pd
import pytz
import schedule
import time

timezone = pytz.timezone('Asia/Ho_Chi_Minh')

def update_Notion_board(obj, label, data):
    latest_row = data[-1]
    latest_price = latest_row[label]
    latest_date = pd.to_datetime(latest_row["Date"])

    obj.update_gia_hien_tai(latest_price)
    obj.update_ngay_cap_nhat_gan_nhat(latest_date.strftime(constants.DATE_FORMAT))
    if len(data) > 1:
        pre_row = data[-2]
        pre_price = pre_row[label]

        obj.update_tinh_trang("Tăng" if latest_price > pre_price else "Giảm")

def task():
    current = pd.Timestamp.now(tz=timezone).tz_localize(None)
    
    from_date = current - pd.Timedelta(days=constants.DAYS_GAP_FOR_TRAIN)
    old_data = database_helper.get(from_date.strftime(constants.DATE_FORMAT))
    
    is_url_accessible = False
    for i in range(10):
        if crawler_helper.is_url_accessible(constants.URL):
            is_url_accessible = True
            break

    if not is_url_accessible:
        Notion_helper.log(current.strftime(r'%d-%m-%Y %H:%M:%S'), "Không vào web được")
        sum_data = old_data
        new_data = None
        print("Không vào web được")
    else:

        if old_data is None or len(old_data) == 0:
            new_data = crawler_helper.get_data()  # dict
            sum_data = new_data
            update_Notion_board(Notion_helper.XANG_RON_95_III, "Xăng RON 95-III", sum_data)
            update_Notion_board(Notion_helper.XANG_E5_RON_92_II, "Xăng E5 RON 92-II", sum_data)

            Notion_helper.send_notification()
        else:
            latest_date = pd.to_datetime(old_data[-1]["Date"]) 
            new_data = crawler_helper.get_data(latest_date)  # dict

            if len(new_data) > 0:
                sum_data = old_data + new_data

                update_Notion_board(Notion_helper.XANG_RON_95_III, "Xăng RON 95-III", sum_data)
                update_Notion_board(Notion_helper.XANG_E5_RON_92_II, "Xăng E5 RON 92-II", sum_data)

                Notion_helper.send_notification()
            else:
                sum_data = old_data
    
    
    latest_date = pd.to_datetime(sum_data[-1]["Date"])
    Notion_helper.XANG_RON_95_III.update_so_ngay_cap_nhat_gan_nhat((current - latest_date).days)
    Notion_helper.XANG_E5_RON_92_II.update_so_ngay_cap_nhat_gan_nhat((current - latest_date).days)

    predict = predict_helper.predict(sum_data, current)

    database_helper.post(predict, new_data)
    print("Done")
def main():
    schedule.every().day.at(constants.TIME_RUN).do(task)
    while True:
        schedule.run_pending()
        time.sleep(10)
if __name__ == "__main__":
    main()