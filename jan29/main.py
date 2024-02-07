from calc import calculate_revenue
from constants import PRICES, EXPENSES, SALES

print('what would you like to call your store?')
store_name = input()
print('Here are the set prices:')
"""
PRICES = {
  'apple': 1000, # 한개
  'grapes': 1500, # 한 뭉치
  'oranges': 10000, # 한 박스
  'watermelon': 30000, # 한개
  'melon': 4000, # 2개
  'pear': 1400, # 한개
}
"""
for fruit in PRICES:
## print list of prices
  # print(fruit + ": " + str(PRICES[fruit]) + "원")
  print(f'{fruit}: {PRICES[fruit]}원')

while(True):
  print('pick an option')
  print('total revenue - 1')
  print('total - 2')
  result_type = input()
  if (result_type == '1'):
    revenue = calculate_revenue()
    print(f'Total Revenue is: {revenue}')
    print('')
  # elif (result_type == 2):
  #   revenue = calculate_revenue()
  #   expenses = calculate_expense()
  #   # print(f'Revenue minus expense is: {}')
  else:
    print('invalid option, please reselect.')

