from datetime import datetime, timedelta

startdate = datetime(2024, 1, 1)

for x in range(366):
    newdate = startdate + timedelta(days=x)
    print('# ' + str(newdate.date()) + ' D' + str(newdate.strftime('%j')) + ' W' + str(newdate.strftime('%V')) + '-' + str(newdate.strftime('%u')))

