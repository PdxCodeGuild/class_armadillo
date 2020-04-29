
# Lab 21: Rain Data


The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly:  http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

```
Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

```

Download one of these files and write a function to load the file. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.

To parse the dates, use [datetime.strptime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior). This allows for easy access to the year, month, and day as `int`s. Below I've shown how to parse an example string, resulting in a [datetime](https://docs.python.org/3.6/library/datetime.html#date-objects) object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use [datetime.strftime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).

```python
import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
```

## Version 2

Now that you've successfully extracted the data, let's done some statistics.

### 1. Calculate the mean of the data:

![mean](https://wikimedia.org/api/rest_v1/media/math/render/svg/c7740a0aa91314dbf006e8583ce6f61585e3aab6)


### 2. Use the mean to calculate the standard deviation, which is a measure of how "spread out" the data is:

![standard_deviation](https://www.gstatic.com/education/formulas/images_long_sheet/sample_standard_deviation.svg)

68.2% of the data falls within 1 standard deviation of the mean.

![bell_curve](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/500px-Standard_deviation_diagram.svg.png)

### 3. Find the day which had the most rain.

### 4. Find the year which had the most rain on average.


## Version 3

Using `matplotlib` create a chart of the dates and the daily totals for a given year. The `x_values` will be a list of dates, The `y_values` are a list of the daily totals. If you don't have matplotlib installed, run `pip install matplotlib`. You can learn more about matplotlib [here](https://matplotlib.org/2.1.0/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py).

```python
import matplotlib.pyplot as plt
...
plt.plot(x_values, y_values)
plt.show()
```

Some charts you can make are:
- all the data, date vs daily total
- monthly totals, average across multiple years
- total yearly rainfall, year by year


## Version 4 (optional)

Use regular expressions to pull all the .rain files from the html source of the main page and do statistics on all of them.
