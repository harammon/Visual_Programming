"""
 * 파일명 : problem2.py
 * 작성일 : 2020년 11월 3일
 * 작성자 : 문헌정보학과 20142611 이하람
 """
import random

def lotto_generator():
    global lotto_num
    while True:
        num = random.randrange(1, 46)
        lotto_num.add(num)
        if len(lotto_num)==6:
            lotto = list(lotto_num)
            lotto_num.clear()
            break
    return lotto

lotto_num = set()
while True:
    n = int(input("원하는 숫자를 입력하세요. (1~100) : "))
    a = 1
    if n>=1 and n<=100:
        while n:
            lotto_list = lotto_generator()
            print("%d회 : " %a, end = "")
            for j in range(6):
                print(lotto_list[j], end = " ")
            print("")
            n -= 1
            a += 1
        print("이 주의 로또 번호 : ", end = "")
        for i in range(6):
            print(lotto_list[i], end = " ")
        print("")
        print("")
    else:
        print("잘 못 입력하셨습니다. (1~100의 수를 입력하세요.")
