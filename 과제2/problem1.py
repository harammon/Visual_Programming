"""
 * 파일명 : problem1.py
 * 작성일 : 2020년 10월 21일
 * 작성자 : 문헌정보학과 20142611 이하람
 """
import random

comWin = 0
userWin = 0
roundNum = 1
choice = ("가위", "바위", "보")
print("가위바위보 게임")
while (comWin !=3) and (userWin !=3):   
    print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(comWin, userWin, userWin, comWin))
    print("(라운드 %d)" %roundNum)
    print("컴퓨터가 결정했습니다.")
    comIndex = random.randint(0,2)
    user = input("무엇을 내시겠습니까? (가위, 바위, 보)  ")
    userIndex = choice.index(user)
    if comIndex - userIndex == 0:
        print("컴퓨터는", choice[comIndex], "당신은", choice[userIndex], "비겼습니다.")
        roundNum += 1
    elif (comIndex - userIndex == 1) or (comIndex - userIndex == -2):
        print("컴퓨터는", choice[comIndex], "당신은", choice[userIndex], "컴퓨터가 이겼습니다.")
        comWin += 1
        roundNum += 1
    else:
        print("컴퓨터는", choice[comIndex], "당신은", choice[userIndex], "당신이 이겼습니다.")
        userWin += 1
        roundNum += 1
if (comWin == 3):
    print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(comWin, userWin, userWin, comWin))
    print("최종 우승자는 컴퓨터입니다.")
if (userWin == 3):
    print("컴퓨터 : %d승 %d패, 당신 : %d승 %d패" %(comWin, userWin, userWin, comWin))
    print("최종 우승자는 당신입니다.")
