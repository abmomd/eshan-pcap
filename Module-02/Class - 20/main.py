# DateTime and Time Module:

from datetime import date,time
import time

st_time = time.time()  # Code Execution starts
# Date Class has --> Year, Month and Day.


d = date(2026,6,25)
d = date.today()
print(d)
print(date.today())

# time.sleep(3.5)

# Accessing the attributes:
# All this attributes are read only. You can not update this via d.year = 2030

print("Year : ",d.year)
print("Month : ",d.month)
print("Day : ",d.day)

# Time --> unix TimeStamp.
# A timestamp represents:
# January 1, 1970
# 00 : 00 : 00 UTC
# EST is UTC - 4

# This date is called as unix Epoch

print("Epoch :" , time.time())
end_time = time.time() # Code Execution is completed
print("Total time : ",end_time-st_time)

# Epoch : 1783384966.894606
# Epoch : 1783385004.398574
# Total time :  6.699562072753906e-05
# Total time :  1.0053439140319824
# Total time :  3.505404233932495

# Converting Timestamp to Date:

timeStamp = time.time()

d = date.fromtimestamp(timeStamp)
print(d)

from datetime import time
# Time Class --> hour,minute and seconds
t = time(6,20,30)
print(t)
print("Hour : ",t.hour)
print("Minute : ",t.minute)
print("Second : ",t.second)

# Traffic Light --> loop of 3 colours for different amount of time
# Green --> 30 Sec
# Red --> 120 sec
# Yellow --> 10 Sec
# time.sleep(10)

# DateTime Class
from datetime import datetime

dt = datetime(2026,7,8,13,20,30)
print(dt)
print(datetime.now())

# Changing Format --> strftime
d = date(2026,7,18)
print(d) # By Default it print "2026-07-18"
# 2026/07/18
# 20260718
# Directive	Meaning	Example
# %Y	Year	2025
# %m	Month	07
# %d	Day	08
# %H	Hour	15
# %M	Minute	30
# %S	Second	45

# Date Arithmetic

from datetime import date
d1 = date(2011,6,27)
d2 = date.today()
diff = d2-d1 # Time Delta
print("Days Old: ",diff)
print("Months Old: ", (diff//365)*12)
print("Years Old: ", diff//365)

# print(d.strftime("%Y/%m/%d"))
# print(d.strftime("%Y%m%d"))
