from test import calculate_points

# 지정된 데이타
물어보는수 = 2
points_table = {
  'toronto': 60000,
  'tokyo': 1000,
  'paris': 80000,
  'quatar': 2000000
}

# 물어보는 수 따라 이 질문들이 반복됩니다
while 물어보는수 > 0:
  # step 1: 돈 얼마인지 물어보고 모닝캄 멤버인지 물어보기
  print('how many points can I get?')
  money = int(input())
  print('are you a morning calm member? (Y/N)')
  morning_calm = input()

  # step 2: 포인트 얼마나 받았는지 알려주기
  print('earned points:')
  point_earned = calculate_points(money)
  print(point_earned)
  # step 3: 어떤나라고 갈수있는지 물어보기
  print('어떤 나라로 여행가고 싶으신가요?')
  country = input() # 예시: japan
  morning_calm_dc = 500
  points_needed = points_table[country] # 예시: 1000
  남은포인츠 = point_earned - points_needed # 예시: 300
  모닝캄전용_남은포인츠 = 남은포인츠 + morning_calm_dc # 예시: 30200
  # step 4: 받은 포인트로 원하는 나라로 갈수있는지 알려주기
  if 남은포인츠 >= 0:
    print('갈 수 있습니다.')
  elif 남은포인츠 < 0 and 모닝캄전용_남은포인츠 >= 0:
    print(str(abs(남은포인츠)) + '만큼 모자라 갈 수 없습니다. 하지만 모닝캄 멤버 하시면 갈수있습나다')
  else:
    print(str(abs(남은포인츠)) + '만큼 모자라 갈 수 없습니다.')
  물어보는수 -= 1