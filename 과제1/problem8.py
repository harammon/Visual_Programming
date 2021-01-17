"""
 * 파일명 : 8.py
 * 작성일 : 2020년 10월 9일
 * 작성자 : 문헌정보학과 20142611 이하람
 """

from math import sin, radians
for i in range(1, 25):
    space=round(sin(radians(i * 15)) * 10) + 10
    print(" "*space, end="")
    print("*")

