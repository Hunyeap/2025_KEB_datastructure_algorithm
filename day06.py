# Assignment day06
# v1.5) https://github.com/inhadeepblue/2024_KEB_datastructure_algorithm 의
# v0.7 guess number 예제를 자동화하고 로그파일(guess.txt)을 남기도록 코드를 수정하시오.
# 단, 해당 프로그램이 로그시간을 갖도록 한다
import random
import time

def measure_time(func):
    """함수 실행 시간을 측정하는 데코레이터"""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 시작 시간 기록
        result = func(*args, **kwargs)  # 원래 함수 실행
        end_time = time.time()  # 종료 시간 기록
        elapsed_time = end_time - start_time  # 실행 시간 계산
        print(f"⏱ {func.__name__} 실행 시간: {elapsed_time:.6f}초")
        return result
    return wrapper
from inspect import stack

@measure_time
def guess_number(low, high, answer, chance) -> int:
    mid =  (low+high) // 2
    print(f'Guess number is {mid}')
    fp.write(f'Guess number is {mid}\n')
    while chance != 0:
        if mid == answer:
            print(f'You win. Answer is {answer}')
            fp.write(f'You win. Answer is {answer}\n')
            return
        elif mid > answer:
            chance = chance - 1
            print(f'{mid} is bigger. Chance left : {chance}')
            fp.write(f'{mid} is bigger. Chance left : {chance}\n')
            return guess_number(low, mid-1, answer, chance)
        else:
            chance = chance - 1
            print(f'{mid} is lower. Chance left : {chance}')
            fp.write(f'{mid} is lower. Chance left : {chance}\n')
            return guess_number(mid+1, high, answer, chance)
    else:
        print(f'You lost. Answer is {answer}')
        fp.write(f'You lost. Answer is {answer}')


if __name__ == "__main__":
    low = 1
    high = 100
    chance = 7
    answer = random.randint(low, high)
    with open('guess.txt', 'w') as fp:
        guess_number(low, high, answer, chance)