"""
 * 파일명 : problem3.py
 * 작성일 : 2020년 10월 21일
 * 작성자 : 문헌정보학과 20142611 이하람
 """
while True:
    result = 0
    userInput = input("수식을 입력하세요 : ")
    a = userInput.replace("-", "+-")
    if a[0] == '+':
        a = a[1:]
    b = a.split("+")
    for i in b:
        result += int(i)
    print("결과는", result)
