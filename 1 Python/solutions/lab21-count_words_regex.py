





import requests
import re



rain_text = '''
WPCL Rain Gage - 6543 N. Burlington Ave.

PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
Data are the number of tips of the rain gage bucket.
Each tip is 0.01 inches of rainfall.
 [-, missing data]
Dates and times are PACIFIC STANDARD TIME.

            Daily  Hourly data -->
   Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
------------------------------------------------------------------------------------------------------------------
20-DEC-2018     0    0   0   0   0   0   0   0   0   0
19-DEC-2018     1    0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
18-DEC-2018    95    7   3   4  14  21  13  14   8   2   0   0   0   0   0   0   3   1   1   4   0   0   0   0   0
17-DEC-2018    39    1   0   0   3   1   0   0   0   0   0   0   0   0   0   0   2   2   6   5   4   2   4   4   5
16-DEC-2018    36    3   3   2   2   1   2   1   0   1   0   0   2   5   8   4   2   0   0   0   0   0   0   0   0
15-DEC-2018     7    0   0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   4   1
14-DEC-2018     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   0   0   0   0
13-DEC-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
12-DEC-2018     4    0   2   0   1   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
11-DEC-2018    67    0   0   5   3   1   0   0   0   0   0   0   0   0   3   6  13   3  12   9   3   3   1   2   3
10-DEC-2018     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   0   0   0   0
09-DEC-2018    49    0   0   0   0   0   0   0   0   0   0   3   6   7   5   4   4   4   6   5   4   1   0   0   0
08-DEC-2018     4    1   2   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
07-DEC-2018     2    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   2
06-DEC-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
05-DEC-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
04-DEC-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
03-DEC-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
02-DEC-2018     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   0
01-DEC-2018     8    3   5   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
30-NOV-2018    55    0   0   0   0   1   0   0   2   0   1   1   0   0   0   1  26  10   1   1   1   1   4   5   0
29-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
28-NOV-2018    31    0   0   0   0   0   0   1   1   4  10   3   1   4   5   1   0   1   0   0   0   0   0   0   0
27-NOV-2018    64    2  15   9   3  14  16   3   0   0   1   0   0   0   0   0   0   1   0   0   0   0   0   0   0
26-NOV-2018    16    0   0   0   0   0   1   0   0   0   0   0   1   0   0   0   0   1   0   1   2   1   3   4   2
25-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
24-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
23-NOV-2018    50    0   0   1   1   1   0   1   0   3   8  18   5   5   3   0   0   0   3   1   0   0   0   0   0
22-NOV-2018    77    4   3   2   0   0   0   0   0   0   0   1   5  22  15   1   1   1   0   4   1   0   1  14   2
21-NOV-2018     6    0   0   0   0   0   0   0   0   0   0   2   0   2   1   0   0   0   0   0   0   0   0   0   1
20-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
19-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
18-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
17-NOV-2018     1    0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0
16-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
15-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
14-NOV-2018     2    0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   0
13-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
12-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
11-NOV-2018     1    0   0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
10-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
09-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
08-NOV-2018     1    0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
07-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
06-NOV-2018     2    0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   0   0   0   0   0   0
05-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
04-NOV-2018    14    0   0   3   4   2   2   2   0   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0   0
03-NOV-2018     2    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   1   0   0   0   0   0   0
02-NOV-2018    11    0   0   0   5   3   2   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
01-NOV-2018     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
31-OCT-2018    12    4   4   0   1   1   0   0   0   0   0   0   0   0   0   0   1   1   0   0   0   0   0   0   0
30-OCT-2018     3    0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   1
29-OCT-2018    29    6   1   3   0   0   0   1   0   0   0   0   0   0   3  15   0   0   0   0   0   0   0   0   0
28-OCT-2018    10    1   1   4   0   0   0   0   0   0   0   0   0   0   2   1   0   1   0   0   0   0   0   0   0
27-OCT-2018   198    0   0   0   0   0   0   0   0   0   0   0   0   0   0  18  17  19  11   8   5  17  63  38   2
26-OCT-2018    55    0   4   2   2   2   0   0   0   0   1   0  26   1   0   1   0   0   3   4   4   4   0   1   0
25-OCT-2018    36    0   0   0   0   4   1   1   0   0   0   1   5   2   1   3   1   4   2   7   3   0   1   0   0
24-OCT-2018     1    1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
23-OCT-2018     6    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   3   3   0   0   0   0   0   0
'''


regex = '(\d{2}-\w{3}-\d{4})\s+(\d+)'

print(re.findall(regex, rain_text))






response = requests.get('http://www.gutenberg.org/files/58500/58500-0.txt')
text = response.text

regex = '[a-zA-Z’\'.]+'

words = re.findall(regex, text)

print(len(words))







