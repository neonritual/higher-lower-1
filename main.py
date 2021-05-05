from game_data import data
from random import randint

# print("&&&&&& HIGHER or LOWER &&&&&&\n")
# print(f"Compare A: {data[choice_a]['name']}, a {data[choice_a]['description']} from {data[choice_a]['country']}.")
# print(f"pssst it's {data[choice_a]['follower_count']}")
# print("--------VS---------")
# print(f"Against B: {data[choice_b]['name']}, a {data[choice_b]['description']} from {data[choice_b]['country']}.")
# print(f"pssst it's {data[choice_b]['follower_count']}")



original_points = 0
def calculate_answer(x, y):

  if x > y:
    return "a"
  elif y > x:
    return "b"

points = original_points

def check_answer(answer,guess,points):
  if guess == answer:
    print("yeah")
    return points + 1
  elif guess != answer:
    print("nah")

def calculate_points(add):
    score = 0
    score += add
    return score


print("hi")

def run_game(answer=''):

  # 名前が表示される。ABのどちらが多いか比べる
  # 多い場合は正解　Aに答えが入る
    # ポイントが一つ増える
    # Bにランダムな人が入ってゲームが再スタート
  # 少ない場合は失敗。ゲーム終了

  # 最初だけ
  if answer == '':
    choice_a = randint(1, len(data) - 1) 
    choice_b = randint(1, len(data) - 1) 
  else:
    choice_a = answer
    choice_b = randint(1, len(data) - 1)

  print(f"test: a is {data[choice_a]['follower_count']}, b is {data[choice_b]['follower_count']}")

  answer = calculate_answer(data[choice_a]['follower_count'], data[choice_b]['follower_count'])
  guess = input("A or B? ").lower()
  check_answer(answer, guess, points)
  
  if data[choice_b]['follower_count'] > data[choice_a]['follower_count']:
    choice_a = choice_b
  elif data[choice_b]['follower_count'] < data[choice_a]['follower_count']:
    choice_a = choice_a
  

  print(f"test: a is {data[choice_a]['follower_count']}, b is {data[choice_b]['follower_count']}, points are {points}")
  run_game(choice_a)
  

run_game()
