from constants import PRICES,SALES


def calculate_revenue():
  total = 0
  for day in SALES:
    print(f'value: {day}')
    for fruit in SALES[day]:
      total = SALES[day][fruit] * PRICES[fruit] + total
  return total
