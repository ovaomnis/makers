import time, datetime
with open('rows_300.csv', 'w') as file:
    for i in range(1, 301):
        localtime = datetime.datetime.now()
        sec = localtime.strftime('%S')
        milli = localtime.strftime('%f')
        file.write(f'{i},{sec},{milli}\n')
        time.sleep(0.01)