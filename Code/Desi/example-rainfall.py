import re

def get_rainfall_amounts(name_of_months):
  months_in_a_year = 12 
  total_rainfall_list = []

  for current_monthly_index in range(months_in_a_year):
      monthly_rainfall = int(input("Enter rainfall amount for " + names_of_months [current_month_index]))
      total_rainfall_list.append(monthly_rainfall)

  return total_rainfall_list

  print(total_rainfall_list)

  d+-\w+-\d+\s\d