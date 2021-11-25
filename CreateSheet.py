import datetime
import schedule
import time

import openpyxl


def job():

    book = openpyxl.Workbook()

    sheet = book.active

    tdatetime = datetime.datetime.now().date
    tstr = tdatetime.strftime('%Y/%m/%d')

    print(tstr)

    sheet.title = datetime.date.today() + '～' + (datetime.date.today() + 6)

    print(datetime.date.today() + '～' + (datetime.date.today() + 6))

schedule.every().day.at("21:48").do(job)

while True:
    schedule.run_pending()
    time.sleep(5)
