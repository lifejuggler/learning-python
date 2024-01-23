# 술먹을수있는 나이 계산하기


def is_drink_age(age):
  restricted_age = 18
  if restricted_age > age:
    return False # cannot
  else:
     return True

def drink_calculator():
  name = str(input('what is your name'))
  age = int(input("what is your age?"))
  can_drink = is_drink_age(age)
  if can_drink:
   print(f"{name}님은 술 드실수있습니다")
  else:
   print(f"{name}님은 술 못 드십니다")

# 기본 소개 예시
def basic_intro():
    print('what is your name?')
    name = input()
    print('hello ' + name + ' how are you?')
    print('how old are you?')
    age = input()
    print( 'you are ' + age + 'certainly?')
# basic_intro()

# name = ['T', 'o', 'm'] # 3
# name = 'Tom'
# name[0] # T
# name[2] # m
# 이름 첫 캐릭터랑 이름 길이
def first_letter_reply():
  print('what is your name?')
  name = str(input())
  print('your first letter is ' + name[0])
  print('name length is ' + str(len(name)))

# first_letter_reply()
# This is a test sentence
def character_number_calculator():
  print('give me a word')
  word = str(input())
  print('개수는 ' + str(len(word)) + '개 입니다.')
# character_number_calculator()

def word_number_calculator():
  print('give me a sentence')
  sentence = str(input())
  print('개수는 ' + str(sentence.split(' ')) + '개 입니다.')
  # 여기서 단어 'is'가 들어가는지는 어떻게 알까요?
  if not('is' in sentence):
    print('sentence has no "is"')
  else:
    print('setence has "is"')
word_number_calculator()