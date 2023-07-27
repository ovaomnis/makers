from datetime import datetime
import calendar

mm = datetime.now().month
yy = datetime.now().year

print(calendar.monthrange(yy, mm))
