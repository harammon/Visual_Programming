"""
 * 파일명 : 4.py
 * 작성일 : 2020년 10월 3일
 * 작성자 : 문헌정보학과 20142611 이하람
 * 출력예시 : 데이터를 입력하세요.(입력을 마치려면 0을 입력하세요.)
              90
              55
              86
              79
              91
              0
              결과 : 55 79 86 90 91 (5개)
 """

data=[]
print("데이터를 입력하세요.(입력을 마치려면 0을 입력하세요.) ")
while True:
    inputNum = int(input())
    if inputNum ==0:
        data.sort()
        print("결과 : ", end="")
        for i in data:
            print(i, end=" ")
        print("(", end="") 
        print(len(data), end="")
        print("개)")
        break
    else:
        data.append(inputNum)

