
import re
from datetime import datetime

text = '''
Hayden Island Rain Gage - 1740 N. Jantzen Beach Ctr.

PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
Data are the number of tips of the rain gage bucket.
Each tip is 0.01 inches of rainfall.
 [-, missing data]
Dates and times are PACIFIC STANDARD TIME.

            Daily  Hourly data -->
   Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
------------------------------------------------------------------------------------------------------------------
01-MAY-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0
30-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
29-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
28-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
27-APR-2020     3    0   2   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
26-APR-2020     5    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   2   3   0
25-APR-2020    16    0   0   0   0   0   0   5   8   2   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0
24-APR-2020     2    0   0   0   0   0   0   0   0   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0
23-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
22-APR-2020    23    0   0   0   0   2   4   0   3   6   3   0   4   0   0   1   0   0   0   0   0   0   0   0   0
21-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
20-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
19-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
18-APR-2020    18    0   0   0   0   0   0   0   0   1   1   1   2   0   0   1   1   0   4   6   0   0   0   0   1
17-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
16-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
15-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
'''




# represent data as a list of dictionaries, with a tuple for the date
data = [{
    'date': (2020, 5, 1),
    'total': 0
},{
    'date': (2020, 4, 30),
    'total': 0
},
...
{
    'date': (2020, 4, 25),
    'total': 16
}]

# represent data as a list of tuples with datetime objects
data = [
    (datetime(2020, 5, 1), 0),
    (datetime(2020, 4, 30), 0)
]

# represent the data as a list of instances of DailyRain
class DailyRain:
    def __init__(self, date, total):
        self.date = date
        self.total = total

