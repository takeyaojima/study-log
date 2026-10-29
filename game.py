import random

answer = random.randint(1,1000)
count = 0 

while True:
    guess = int(input("1~1000の数は?: "))
    count += 1
    if guess < answer:
        print("もっと大きい！")
    elif guess > answer:
        print("もっと小さい！")
    else:
        print(f"正解!{count}回目でした")
        break