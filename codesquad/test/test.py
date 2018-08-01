# 숫자 야구 게임
from random import randint


def generate_com_numbers():
    """1부터 9까지 임의의 숫자 세개를 생성한다"""
    com_hand = []
    while len(com_hand) < 3:
        random_number = randint(1, 9)
        if random_number not in com_hand:
            com_hand.append(random_number)
    return com_hand


def count_numbers(com, user):
    """ 스트라이크, 볼 판단 """
    strike = 0
    ball = 0
    result = []

    for index in range(len(user)):
        if com[index] == int(user[index]):
            strike += 1
        elif str(com[index]) in user:
            ball += 1

    result.append(strike)
    result.append(ball)

    return result


def score(strike, ball):
    """ 스트라이크, 볼 판정 """
    if strike > 0 and ball > 0:
        print("%d 스트라이크 %d 볼" % (strike, ball))
    elif strike > 0:
        print("%d 스트라이크" % strike)
    elif ball > 0:
        print("%d 볼" % ball)
    else:
        print("낫싱")


# 컴퓨터의 패
com_hand = generate_com_numbers()

# 게임 진행
strike = 0

while strike < 3:
    guess_number = input("숫자를 입력해주세요 ex)123 : ")
    count = count_numbers(com_hand, guess_number)

    strike = count[0]
    ball = count[1]

    score(strike, ball)

print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")

