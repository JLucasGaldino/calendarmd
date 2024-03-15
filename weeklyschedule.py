import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('calfile', type = open, help = 'the calendar file')

today = datetime.today().date()
nextweek = (datetime.today() + timedelta(days=7)).date()

with open('./calendar.md', 'r') as calendar:
    lines = calendar.readlines()
    for row in lines:
        starttarget = str(today)
        endtarget = str(nextweek)
        if row.find(starttarget) != -1:
            todayindex = lines.index(row)
            print(lines[todayindex])
        if row.find(endtarget) != -1:
            nextweekindex = lines.index(row) + 1
            print(lines[nextweekindex])
    delta = nextweekindex - todayindex
    for x in range(delta):
        print(lines[todayindex + x])

