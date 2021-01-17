"""
 * 파일명 : 7.py
 * 작성일 : 2020년 10월 3일
 * 작성자 : 문헌정보학과 20142611 이하람
 """

import random

comChoiceList=["가위", "바위", "보"]
comWin=0
userWin=0
roundNum=1
print("가위바위보 게임")
while(True):
    print("컴퓨터 : ", comWin, end="")
    print("승", userWin, end="")
    print("패,  ", end="")
    print("당신 : ", userWin, end="")
    print("승", comWin, end="")
    print("패  ")
    print("(라운드", roundNum, end="")
    print(")")
    comChoice=comChoiceList[random.randint(0,2)]
    print("컴퓨터가 결정했습니다.")
    userChoice=input("무엇을 내시겠습니까? (가위, 바위, 보) ")

    if comChoice=='가위':
        if userChoice=='가위':
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 비겼습니다.")
            print("")
        elif userChoice=='바위':
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 당신이 이겼습니다.")
            print("")
            userWin+=1
        else: 
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 컴퓨터가 이겼습니다.")
            print("")
            comWin+=1
    if comChoice=='바위':
        if userChoice=='바위':
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 비겼습니다.")
            print("")
        elif userChoice=='보':
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 당신이 이겼습니다.")
            print("")
            userWin+=1
        else: 
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 컴퓨터가 이겼습니다.")
            print("")
            comWin+=1
    if comChoice=='보':
        if userChoice=='보':
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 비겼습니다.")
            print("")
        elif userChoice=='가위':
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 당신이 이겼습니다.")
            print("")
            userWin+=1
        else: 
            print("컴퓨터는", comChoice, end="")
            print(", 당신은", userChoice, end="")
            print(", 컴퓨터가 이겼습니다.")
            print("")
            comWin+=1
    if comWin==3:
        print("컴퓨터 : ", comWin, end="")
        print("승", userWin, end="")
        print("패,  ", end="")
        print("당신 : ", userWin, end="")
        print("승", comWin, end="")
        print("패  ")
        print("최종 우승자는 컴퓨터입니다.")
        break
    if userWin==3:
        print("컴퓨터 : ", comWin, end="")
        print("승", userWin, end="")
        print("패,  ", end="")
        print("당신 : ", userWin, end="")
        print("승", comWin, end="")
        print("패  ")
        print("최종 우승자는 당신입니다.")
        break
    roundNum+=1
 
 



